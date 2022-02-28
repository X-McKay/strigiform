module "postgresql" {
    source = "../modules/rds"
    db_name = local.db_name
    tags = merge(local.tags, {Name = var.db_name})
}
