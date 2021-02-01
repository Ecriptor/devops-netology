# Configure the AWS Provider
provider "aws" {
  region = "us-east-2"
}

data "aws_ami" "ubuntu" {
  most_recent      = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "netology" {
  // какой образ за основу
  ami = data.aws_ami.ubuntu.id
  // тип
  instance_type = "t2.micro"

  // не защищать от удаления по API
  disable_api_termination = false
  // при завершении останавливать инстанс
  instance_initiated_shutdown_behavior = "stop"
  monitoring = false
  // присвоить инстансу публичный ip-адрес
  associate_public_ip_address = true
  // каким будет внутренний ip нашего инстанса
  tags = {
    Name = "DevOps_Netology"
  }
}

//
data "aws_caller_identity" "current" {}

//регион будет как в провайдере
data "aws_region" "current" {}
