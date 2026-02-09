# Event-Driven PDF Processing on AWS

## Project Overview
This project demonstrates an event-driven workflow for processing PDF files using AWS services. The system automatically handles PDF files uploaded to an S3 bucket, processes them using AWS Lambda, and stores metadata in DynamoDB. This setup provides a foundation for automated backend operations with future potential for frontend and API integration.

---

### Phase 1 – S3 Upload & Lambda Trigger

**Goal:** Automatically process PDF files uploaded to S3 using Lambda.

**Steps Completed:**

- **Created S3 Bucket (Source Bucket)**
  - Bucket name: `bucket-uploadfile-source-001`
  - Enabled versioning (optional)
  - Configured trigger for Lambda on `s3:ObjectCreated:Put`
  - Configured event filter for `.pdf` files only

- **Created Lambda Function (Phase 1)**
  - Runtime: Python 3.14
  - Trigger: Source S3 bucket (`bucket-uploadfile-source-001`)
  - Function reads uploaded file from S3  
  - **Python code:** Refer to `lambda_function.py` file uploaded separately

**✅ Outcome:**

- Upload a PDF to source bucket → triggers Lambda → file copied to destination bucket → metadata stored in DynamoDB table `FileProcessingMetadata`
- Binary files handled correctly (no UTF-8 decoding issues)

---

### Phase 2 – DynamoDB Metadata Storage

**Goal:** Track processed file metadata for future reference.

**Steps Completed:**

- Created DynamoDB table
  - Table name: `FileProcessingMetadata`
  - Primary key: `FileName` (string)
  - Other fields stored: `ProcessedFileName`, `SourceBucket`, `DestinationBucket`, `UploadTime`, `FileSize`
- Integrated DynamoDB write in Lambda
- Every processed PDF’s metadata stored in DynamoDB
- Allowed tracking of processed files in event-driven workflow

**✅ Outcome:**

- Successfully implemented event-driven processing
- Every new PDF upload is automatically copied and tracked

---

### Phase 3 – Event-Driven Processing Achieved

**Goal:** Ensure fully automated workflow from S3 upload to processed output with tracking

**Workflow Achieved:**

1. Upload PDF to S3 Source Bucket  
2. Lambda triggered automatically  
3. Lambda reads file and uploads to Destination Bucket  
4. Metadata stored in DynamoDB  

**Diagram (simplified):**
[S3 Source Bucket] --(PUT)--> [Lambda] --(put_object)--> [S3 Destination Bucket]
|
+--(put_item)--> [DynamoDB Table]


**✅ Outcome:**

- Event-driven workflow is fully functional
- Frontend/API integration is planned as future work

---

### Future Scope

- Integrate frontend and API to allow direct browser uploads and downloads  
- Implement PDF merging functionality in Lambda  
- Secure API access and improve user interface  

**✅ Conclusion:**

- Achieved: Event-driven workflow for PDFs  
- Upload to S3 → Lambda triggered → processed file stored → metadata tracked  

---

## Author
**Umesh Saini**  
**Internship Project**
