variable "cidr" {
    type = str
    default = "10.99.0.0/16"
}

variable "public_subnets" {
    default = ["10.99.0.0/24", "10.99.1.0/24", "10.99.2.0/24"]
}
variable "private_subnets" {
    default = ["10.99.3.0/24", "10.99.4.0/24", "10.99.5.0/24"]

}

variable "database_subnets" {
    default = ["10.99.7.0/24", "10.99.8.0/24", "10.99.9.0/24"]
}


variable "create_db_subnet_group" {
    default = true
}

variable "enable_dns_hostnames" {
    default = true
}

variable "enable_dns_support" {
    default = true
}
