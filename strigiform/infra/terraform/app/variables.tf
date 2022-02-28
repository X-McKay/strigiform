variable "region" {
  default     = "us-east-1"
  description = "AWS region"
}

variable "db_name" {
  type=string
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

variable "tags" {

  default = {
    "owner"       = "strigiform"
    "project" = "strigiform"
    "created_by" = "terraform"
  }
}
