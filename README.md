# One Rupee Care Project Documentation

## Project Title

**One Rupee Care: Micro-Contributions for Student Health Insurance and Social Good**

## Overview

One Rupee Care is a web-based platform designed to enable students to contribute a small amount — just ₹1 per day — toward a collective health insurance fund. This fund provides financial protection for students in case of medical emergencies. Additionally, any surplus collected beyond the insurance payouts is transparently utilized for social welfare initiatives benefiting the student community and society at large.

## Purpose and Motivation

Healthcare can be expensive, and many students lack adequate insurance coverage. One Rupee Care addresses this issue by making health insurance affordable and accessible through daily micro-contributions. It promotes a culture of collective responsibility and social welfare by pooling small amounts from many to create a significant impact. The project also focuses on transparency and trust by providing clear, real-time insights into fund collection and expenditure.

## Objectives

* **Affordable health coverage:** Enable students to access health insurance with minimal daily contribution.
* **Transparent fund management:** Display real-time collection and expenditure reports to users.
* **Social good:** Utilize leftover funds for community welfare projects such as health camps, education drives, or scholarships.
* **User-friendly interface:** Simplify contribution tracking and claims through an intuitive web app.
* **Trust building:** Ensure transparency through digital audit trails and fund usage reports.

## Key Features

### 1. User Registration and Authentication

* Secure sign-up/login using email or student ID.
* Profile management with personal and payment details.

### 2. Daily Micro-Contribution System

* Automatic or manual payment option for ₹1 per day.
* Multiple payment gateways integration (UPI, debit/credit cards, wallets).
* Daily reminders and notifications for contribution.

### 3. Health Insurance Coverage

* Details of insurance plan available to all users.
* Easy claim submission process via the app with document upload.
* Claim status tracking and notifications.

### 4. Fund Management and Transparency

* Dashboard showing total contributions collected.
* Breakdown of expenses for insurance claims and social welfare.
* Real-time reports on leftover funds.
* Audit trail for all transactions ensuring accountability.

### 5. Social Welfare Initiatives

* Platform to propose and vote on social good projects funded by leftover money.
* Updates and impact reports on funded initiatives.

### 6. Admin Panel

* Manage users, contributions, claims, and social projects.
* Approve/reject claims.
* Generate financial and operational reports.

## Technology Stack

| Component             | Technology/Tool                       |
| --------------------- | ------------------------------------- |
| Frontend              | React.js / Angular / Vue.js           |
| Backend               | Node.js with Express / Django / Flask |
| Database              | MongoDB / MySQL / PostgreSQL          |
| Payment Gateway       | Razorpay / Paytm / Stripe             |
| Authentication        | JWT / OAuth 2.0                       |
| Hosting               | AWS / Azure / Heroku                  |
| Reporting & Analytics | Chart.js / D3.js / Google Analytics   |
| Version Control       | Git (GitHub/GitLab)                   |

## Architecture Diagram

```
[User Browser] <---> [Frontend Web App] <---> [Backend API Server] <---> [Database]
                                      |
                              [Payment Gateway]
                                      |
                                [Insurance Provider]
```

## Data Flow

1. User registers and logs in.
2. User opts in to daily ₹1 contribution and makes payment through integrated gateways.
3. Payment information and user contribution status are stored in the database.
4. Insurance claims are submitted via the app and processed by admin and insurance providers.
5. Leftover funds are allocated for social projects, managed through admin and user voting.
6. Users can track their contribution history, claim status, and social impact reports anytime.

## Security Considerations

* Secure authentication with password hashing and multi-factor authentication (optional).
* Encrypted storage of sensitive user data and payment information.
* HTTPS enforced for all web communications.
* Regular audits and validation of transactions to prevent fraud.

## Benefits

* Makes health insurance affordable and accessible to students.
* Encourages community participation and responsibility.
* Transparent fund utilization builds trust among contributors.
* Supports meaningful social welfare activities benefiting the wider community.

## Future Enhancements

* Mobile app for easier access and notifications.
* Integration with government health schemes for enhanced coverage.
* AI-based fraud detection in claims processing.
* Social gamification features to motivate regular contributions.

## Conclusion

One Rupee Care leverages the power of micro-contributions and transparency to solve critical issues of healthcare affordability and social responsibility among students. It fosters a supportive community where small daily actions collectively make a big difference in health security and social welfare.

---

Would you like me to help you create a **technical manual**, **user guide**, or **presentation slides** for this project as well?
