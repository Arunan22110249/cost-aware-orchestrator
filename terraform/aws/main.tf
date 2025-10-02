terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Minimal VPC and autoscaling group example (study/demo only)
resource "aws_vpc" "demo" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "demo-vpc" }
}

resource "aws_subnet" "demo" {
  vpc_id            = aws_vpc.demo.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = data.aws_availability_zones.available.names[0]
  tags = { Name = "demo-subnet" }
}

data "aws_availability_zones" "available" {}

resource "aws_launch_template" "app_lt" {
  name_prefix   = "demo-lt-"
  image_id      = var.ami_id
  instance_type = var.instance_type

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "app_asg" {
  name                      = "demo-asg"
  max_size                  = var.max_size
  min_size                  = var.min_size
  desired_capacity          = var.desired_capacity
  launch_template {
    id      = aws_launch_template.app_lt.id
    version = "$Latest"
  }
  vpc_zone_identifier = [aws_subnet.demo.id]
  tags = [
    {
      key                 = "Name"
      value               = "demo-asg"
      propagate_at_launch = true
    }
  ]
}
