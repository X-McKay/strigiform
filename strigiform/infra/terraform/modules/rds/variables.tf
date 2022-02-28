variable "instance_name" {
    type    = string
    description = "The name of the database instance"
    default = "strigiform-postgres"
}

variable "storage_encrypted" {
  description = "Specifies whether the DB instance is encrypted"
  type        = bool
  default     = true
}

variable "kms_key_id" {
  description = "The ARN for the KMS encryption key. If creating an encrypted replica, set this to the destination KMS ARN. If storage_encrypted is set to true and kms_key_id is not specified the default KMS key created in your account will be used"
  type        = string
  default     = null
}


variable "instance_class" {
    type    = string
    description = "Size and type of the RDS instance"
    default = "db.t3.micro"
}

variable "allocated_storage" {
    type = number
    description = "The allocated storage in gibibytes"
    default = 5
}

variable "engine_version" {
    type = string
    description = "Version of Postrgres database"
    default = "13.1"
}

variable "db_name" {
    type    = string
    description = "The name of the database"
    default = "strigiform"
}

variable "db_username" {
    type = string
    description = "Username of database"
    default = "strigiform"
}

variable  "db_password" {
type = string
description = "Database password"

validation {
    condition = length(var.db_password >= 8)
    error_message = "Please increase length of password!"
}

}

variable "db_subnet_group_name" {

}

variable "param_family" {
    default = "postgres13"
}

variable "deletion_protection" {
    default = true
}

variable "skip_final_snapshot" {
    default = true
}

variable "maintenance_window" {
    default = "Mon:00:00-Mon:03:00"
}

variable "backup_window" {
    default = "03:00-06:00"
}

variable "backup_retention_period" {
    type = number
    default = 3
}
