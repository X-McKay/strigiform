# Terraform set-up and commands

1.  To get started, initialize terraform

    `terraform init`

2.  After making changes, format and then validate

    `terraform fmt`

    `terraform validate`

3.  To get a cost estimate prior to deploying, run:
    Note: requires setup of [infracost](https://github.com/infracost/infracost)

        `infracost breakdown --path=plan`

4.  Deploy infrastructure

    `terraform apply`

5.  If necessary, teardown infrastructure:

    `terraform destroy`
