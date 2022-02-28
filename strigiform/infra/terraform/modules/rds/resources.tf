resource "aws_db_instance" "postgresql" {

    # DB instance specifications
    identifier          = var.instance_name
    instance_class       = var.instance_class
    allocated_storage    = var.allocated_storage
    engine               = "postgres"
    engine_version       = var.engine_version

    # DB auth
    name                 = var.db_name
    username             = var.db_username
    password             = var.db_password
    iam_database_authentication_enabled = var.iam_db_auth

    # DB security
    db_subnet_group_name   = aws_db_subnet_group.strigiform.name
    vpc_security_group_ids = [aws_security_group.rds.id]
    publicly_accessible    = false
    parameter_group_name = var.parameter_group_name
    storage_encrypted = var.storage_encrypted
    kms_key_id        = var.kms_key_id

    # DB Deletion Protection
    deletion_protection = var.deletion_protection
    skip_final_snapshot    = var.skip_final_snapshot
    maintenance_window = var.maintenance_window
    backup_window      = var.backup_window
    backup_retention_period = var.backup_retention_period


    # DB tags
    tags = var.tags
}


resource "aws_db_parameter_group" "pg_param_group" {
  name   = var.name
  family = var.param_family

  parameter {
    name  = "log_connections"
    value = "1"
  }
}
