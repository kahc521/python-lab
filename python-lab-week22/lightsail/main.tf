terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.61.0"
    }
  }
}

provider "aws" {

  region = "us-east-1"
}


resource "tls_private_key" "lightsail_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}
# Create the Key Pair
resource "aws_lightsail_key_pair" "lightsail_key2" {
  name       = "python"
  public_key = tls_private_key.lightsail_key.public_key_openssh
}
# Save file
resource "local_file" "ssh_key" {
  filename = "python.pem"
  content  = tls_private_key.lightsail_key.private_key_pem
}

resource "aws_lightsail_instance" "server1" {
  name              = "python-server"
  blueprint_id      = "centos_7_2009_01"
  bundle_id         = "medium_1_0"
  availability_zone = "us-east-1a"
  key_pair_name     = "python"
  user_data = file("script.sh")
} 
                        
output "ip" {
  value = aws_lightsail_instance.server1.public_ip_address
}
output "user" {
  value = aws_lightsail_instance.server1.username
}