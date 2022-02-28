# Supporting Resources

data "aws_availability_zones" "available" {}

resource "aws_vpc" "main"{

  name                 = var.name
  cidr                 = var.cidr

  azs                  = data.aws_availability_zones.available.names
  public_subnets       = var.public_subnets
  private_subnets      = var.private_subnets
  database_subnets     = var.database_subnets

  create_database_subnet_group = var.create_database_subnet_group
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_hostnames
  tags = var.tags
}

resource "aws_db_subnet_group" "strigiform" {
  name       = var.name
  subnet_ids = var.public_subnets

  tags = var.tags
}
