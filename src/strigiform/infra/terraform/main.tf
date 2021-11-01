provider "aws" {
  region = var.region
}

locals {
  name   = "strigiform-postgres"
  region = "us-east-1"
  tags = {
    Owner       = "strigiform"
    Environment = "dev"
  }
}

# Supporting Resources

data "aws_availability_zones" "available" {}

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "2.77.0"

  name                 = local.name
  cidr                 = "10.99.0.0/16"

  azs                  = data.aws_availability_zones.available.names
  public_subnets       = ["10.99.0.0/24", "10.99.1.0/24", "10.99.2.0/24"]
  private_subnets      = ["10.99.3.0/24", "10.99.4.0/24", "10.99.5.0/24"]
  database_subnets     = ["10.99.7.0/24", "10.99.8.0/24", "10.99.9.0/24"]

  create_database_subnet_group = true
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = local.tags
}

resource "aws_db_subnet_group" "strigiform" {
  name       = "strigiform"
  subnet_ids = module.vpc.public_subnets

  tags = {
    Name = "Strigiform"
  }
}

resource "aws_security_group" "rds" {
  source  = "terraform-aws-modules/security-group/aws"
  version = "~> 4"

  name        = local.name
  vpc_id = module.vpc.vpc_id

  # ingress
  ingress_with_cidr_blocks = [
    {
      from_port   = 5432
      to_port     = 5432
      protocol    = "tcp"
      description = "PostgreSQL access from within VPC"
      cidr_blocks = module.vpc.vpc_cidr_block
    },
  ]

  tags = local.tags

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "strigiform_rds"
  }
}

resource "aws_db_parameter_group" "strigiform" {
  name   = "strigiform"
  family = "postgres13"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}

resource "aws_db_instance" "strigiform" {

  # DB specifications
  identifier             = "strigiform"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "13.1"

  # DB auth
  username               = "strigiform"
  password               = var.db_password
  iam_database_authentication_enabled = true

  # DB security
  db_subnet_group_name   = aws_db_subnet_group.strigiform.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  publicly_accessible    = true

  # DB Deletion Protection
  deletion_protection = true
  skip_final_snapshot    = true
  maintenance_window = "Mon:00:00-Mon:03:00"
  backup_window      = "03:00-06:00"

  # DB parameter group
  parameter_group_name   = aws_db_parameter_group.strigiform.name

  # DB tags
  tags = {
    Owner       = "strigiform"
    Environment = "dev"
  }
}

module "db_disabled" {
  source = "../../"

  identifier = "${local.name}-disabled"

  create_db_instance        = false
  create_db_subnet_group    = false
  create_db_parameter_group = false
  create_db_option_group    = false
}
