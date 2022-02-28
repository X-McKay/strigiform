locals {
    name   = "strigiform-postgres"
    region = "us-east-1"

    db_name = "strigiform"
    instance_class = "db.t3.micro"
    allocated_storage = 5

    tags = {
        "env" = "dev"
    }

}
