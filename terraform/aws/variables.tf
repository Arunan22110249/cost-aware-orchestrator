variable "aws_region" { default = "us-east-1" }
variable "ami_id" { default = "ami-0c94855ba95c71c99" }
variable "instance_type" { default = "t3.small" }
variable "desired_capacity" { default = 2 }
variable "min_size" { default = 1 }
variable "max_size" { default = 4 }
