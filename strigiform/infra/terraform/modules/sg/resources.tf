
resource "aws_security_group" "db_secgrp" {

  name        = var.name
  description = var.description
  vpc_id = module.vpc.vpc_id

  # ingress with cidr block
  ingress_with_cidr_blocks = [
    {
      from_port   = var.from_port
      to_port     = var.to_port
      protocol    = var.protocol
      description = "DB access from within VPC"
      cidr_blocks = module.vpc.vpc_cidr_block
    },
  ]

  # Ingress configuration
  ingress {
    from_port   = var.in_from_port
    to_port     = var.in_to_port
    protocol    = var.protocol
    cidr_blocks = var.cidr_blocks
  }

  # Egress configuration
  egress {
    from_port   = var.eg_from_port
    to_port     = var.eg_to_port
    protocol    = var.protocol
    cidr_blocks = var.cidr_blocks
  }

  tags = var.tags
}
