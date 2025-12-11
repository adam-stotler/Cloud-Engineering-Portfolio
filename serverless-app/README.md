serverless-app/
├── README.md                  # Project overview, architecture, deployment steps
├── src/                       # Lambda function source code
│   ├── create_item.py
│   ├── get_item.py
│   ├── list_items.py
│   └── delete_item.py
├── iac/                       # Infrastructure as Code (SAM or Terraform)
│   ├── template.yaml          # AWS SAM template (if using SAM)
│   └── main.tf                # Terraform version (if using Terraform)
├── diagrams/                  # Architecture diagrams + visuals
│   └── architecture.png
├── tests/                     # Unit tests for Lambda functions
│   ├── test_create_item.py
│   └── test_list_items.py
└── ut
