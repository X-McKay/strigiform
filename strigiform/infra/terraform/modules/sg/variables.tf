variable "in_from_port" {
    type = int
    default = 5432
    description = "Ingress source port."
}

variable "in_to_port" {
    type = int
    default = 5432
    description = "Ingress destination port."
}

variable "eg_from_port" {
    type = int
    default = 5432
    description = "Egress source port."
}

variable "eg_to_port" {
    type = int
    default = 5432
    description = "Egress destination port."
}

variable "protocol" {
    default = "tcp"
}

variable "cidr_blocks" {
    default = ["0.0.0.0/0"]
}
