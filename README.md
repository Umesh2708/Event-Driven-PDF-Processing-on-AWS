# Event-Driven PDF Processing on AWS

## Project Overview
This project demonstrates an event-driven workflow for processing PDF files using AWS services. The system automatically handles PDF files uploaded to an S3 bucket, processes them using AWS Lambda, and stores metadata in DynamoDB. This setup provides a foundation for automated backend operations with future potential for frontend and API integration.

---

## Phase 1 – S3 Upload & Lambda Trigger

**Goal:** Automatically process PDF files uploaded to S3 using Lambda.

### Steps Completed:

1. **Create Lambda Function**  
   - Name: `PDFProcessingLambda`  
   - Runtime: Python 3.14  

2. **Configure Lambda Permissions**  
   - Go to **Configuration → Permissions → Execution Role**  
   - Click the role link → Attach policies:  
     - `AmazonS3FullAccess` (to read/write S3 files)  
     - `AmazonDynamoDBFullAccess` (to store metadata)  

3. **Create Source S3 Bucket**  
   - Bucket name: `bucket-uploadfile-source-001`  
   - Enable versioning (optional)  

4. **Integrate Lambda with S3**  
   - Configure S3 trigger: **Event type:** `s3:ObjectCreated:Put`  
   - Add event filter for `.pdf` files  

5. **Add Lambda Layer for PDF Processing**  
   - Go to **Lambda → Layers → Create Layer**  
   - Name: `PyPDF2Layer`  
   - Upload `PyPDF2.zip`  
   - Select **Compatible runtime:** Python 3.14  
   - Attach this layer to the Lambda function  

6. **Python Code**  
   - Refer to the uploaded `lambda_function.py`  
   - Handles reading PDFs from S3 and uploading to destination bucket  

### ✅ Outcome:
- Upload a PDF → Lambda triggered → File copied to destination bucket  
- Metadata stored in DynamoDB table `FileProcessingMetadata`  
- Binary PDF files handled correctly (no UTF-8 decoding issues)  

---

## Phase 2 – DynamoDB Metadata Storage

**Goal:** Track processed file metadata for future reference.

### Steps Completed:

1. **Create DynamoDB Table**  
   - Table name: `FileProcessingMetadata`  
   - Primary key: `FileName` (string)  
   - Other fields: `ProcessedFileName`, `SourceBucket`, `DestinationBucket`, `UploadTime`, `FileSize`  

2. **Lambda Integration with DynamoDB**  
   - In the Lambda code, use `boto3` to write metadata  
   - Lambda’s execution role has full access to DynamoDB  
   - Metadata can be explored via **DynamoDB → Explore items**  

### ✅ Outcome:
- Automatic storage of processed file metadata  
- Every new PDF upload is tracked for history  

---

## Phase 3 – Event-Driven Processing Achieved

**Goal:** Fully automated workflow from S3 upload to processed output with tracking

### Workflow Achieved:
1. Upload PDF → **S3 Source Bucket**  
2. Lambda triggered automatically  
3. Lambda reads file and uploads to **Destination Bucket**  
4. Metadata stored in **DynamoDB**

**Diagram (simplified):**

[S3 Source Bucket] --(PUT)--> [Lambda] --(put_object)--> [S3 Destination Bucket]
|
+--(put_item)--> [DynamoDB Table]


### ✅ Outcome:
- Event-driven workflow is fully functional  
- Frontend/API integration is future work  

---

## Dependencies & Setup Steps

- Python 3.14 for Lambda  
- `PyPDF2.zip` for PDF processing  

**Steps to add PyPDF2 in Lambda:**  
1. Go to **Lambda → Layers → Create Layer**  
2. Name: `PyPDF2Layer`  
3. Upload `PyPDF2.zip`  
4. Select compatible runtime: Python 3.14  
5. Attach the layer to the Lambda function  

- AWS SDK (`boto3`) for S3 and DynamoDB interactions  

---

## Future Scope
- Integrate frontend and API to allow direct browser uploads and downloads  
- Implement PDF merging functionality in Lambda  
- Secure API access and improve user interface  

---

## Conclusion

- Achieved a fully **event-driven workflow for PDFs**  
- Upload to S3 → Lambda triggered → Processed file stored → Metadata tracked  
- Ready for frontend/API integration in future iterations  

---

## Author

**Umesh Saini**  
**Internship Project**
