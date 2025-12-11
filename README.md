# Cloud Engineering Portfolio

This portfolio showcases hands-on cloud projects demonstrating skills in serverless architecture, automation, infrastructure-as-code, and systems integration. Each project is designed to be **practical**, **deployable**, and **aligned with real employer expectations**.

---

## Project 1: Serverless Web Application (AWS)
**Architecture:** API Gateway → Lambda → DynamoDB

**Goal:** Build a simple, cost-free, fully serverless CRUD application.

### Overview
This project demonstrates:
- Event-driven design
- Serverless compute (AWS Lambda)
- NoSQL data modeling (DynamoDB)
- IAM permissions scoping
- Infrastructure as Code (AWS SAM or Terraform)

### Architecture Diagram
```
[Client] → [API Gateway] → [Lambda Functions] → [DynamoDB Table]
```

### Step-by-Step Build Guide
1. **Create a DynamoDB Table**  
   - Table name: `Items`
   - Partition key: `id` (String)
   - Billing mode: On-demand (free-tier friendly)

2. **Write Lambda Functions (Python or Node.js)**  
   - `create_item` → PUT new record
   - `get_item` → GET by id
   - `list_items` → Scan the table
   - `delete_item` → Delete by id

3. **Create an API Gateway REST API**  
   - `/items` → POST, GET
   - `/items/{id}` → GET, DELETE
   - Integrate each method with the corresponding Lambda

4. **Add IAM Roles**  
   - Lambda execution role with:
     - `dynamodb:GetItem`
     - `dynamodb:PutItem`
     - `dynamodb:Scan`
     - `dynamodb:DeleteItem`

5. **Deploy with AWS SAM or Terraform**  
   - Write templates to deploy Lambda, API Gateway, and DynamoDB automatically.

6. **Test**  
   - Use Postman or curl
   - Confirm CRUD operations

7. **Publish**  
   - Add architecture diagram
   - Add repo link (GitHub/GitLab)
   - Include code snippets and deployment templates

### Skills Demonstrated
- Serverless design patterns
- IAM least-privilege access control
- NoSQL database best practices
- API design and integration
- Infrastructure as Code

---

## Future Projects (Planned)
- CI/CD Pipeline using GitHub Actions
- Multi-tier VPC with public/private subnets
- Automated CloudWatch monitoring & alarms
- Cost-optimized S3 static site hosting

---

If you want, each new project can be added below to grow this into a complete cloud engineer portfolio.

