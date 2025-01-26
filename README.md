# Strengthening IIoT Cybersecurity Through SSH and VPN Integration

## Project Overview
This project focuses on enhancing the cybersecurity of Industrial Internet of Things (IIoT) systems by integrating Secure Shell (SSH) and Virtual Private Network (VPN) technologies within an AWS environment. It aims to address critical security challenges like unauthorized access, data breaches, and evolving cyber threats, ensuring the secure, scalable, and resilient operation of IIoT infrastructure.

**Note**: This project is funded by the Tamil Nadu State Government, emphasizing its importance in securing critical infrastructure and fostering technological advancements. The project was led by [Your Name], who served as the Team Lead, coordinating efforts across development, implementation, and testing phases.

## Key Features
- **Robust Data Encryption**: Secure data transmission using SSH and VPN to prevent eavesdropping and man-in-the-middle (MITM) attacks.
- **Access Control**: Public key authentication and stringent access rules for secure remote access.
- **Threat Mitigation**: Protection against brute force, DoS, DDoS, and SQL injection attacks.
- **Real-Time Monitoring**: AWS CloudWatch and CloudTrail integration for activity tracking and threat detection.
- **Email Alerts**: SMTP-based email notifications for login events, enabling rapid response to unauthorized access.
- **Scalability**: Configurable VPC, subnets, and security groups to accommodate evolving IIoT needs.
- **Disaster Recovery**: Dual-database architecture with backup and recovery mechanisms.

---


## Introduction

### Purpose
The proliferation of IIoT devices revolutionizes industries by enabling real-time monitoring and predictive maintenance. However, increased connectivity introduces vulnerabilities. This project ensures the confidentiality, integrity, and availability of IIoT data through a multi-layered security approach.

### Motivation
With IIoT systems integral to critical infrastructure, the project aims to:
- Protect sensitive data and intellectual property.
- Ensure compliance with industry standards.
- Mitigate risks of operational disruption due to cyberattacks.

---

## System Architecture

### Components
1. **AWS Cloud Services**: 
   - EC2 instances, VPC, IAM, and S3.
2. **VPN Integration**: 
   - OpenVPN for secure tunneling.
3. **SSH Configuration**:
   - Public key authentication for access control.
4. **Firewall Rules**: 
   - Configured to allow only authorized traffic.
5. **Monitoring and Alerts**:
   - CloudWatch, CloudTrail, and SMTP-based email notifications.

### Architecture Diagram
Refer to `Architecture_Diagram.png` for a visual representation.

---

## Implementation Modules

### 1. **VPC Configuration**
- Create and configure Virtual Private Cloud with appropriate CIDR blocks.
- Attach Internet Gateway and set up route tables.

### 2. **VPN Configuration**
- Deploy OpenVPN to establish secure communication tunnels.
- Restrict SSH traffic to authorized VPN users.

### 3. **SSH Integration**
- Use public key authentication to secure remote access.
- Implement inbound and outbound rules to enforce security policies.

### 4. **Monitoring and Logging**
- Enable CloudWatch for real-time metrics and alarms.
- Use CloudTrail for auditing and compliance.

### 5. **Email Automation**
- Integrate SMTP to send login alerts.
- Python script monitors SSH login attempts and sends alerts with user details.

---

## Security Measures

### Mitigated Threats
- **MITM Attacks**: Encrypted communication using VPN and SSH.
- **Brute Force Attacks**: Restrict access to authorized VPN users.
- **SQL Injection**: Parameterized queries and input validation.
- **DoS and DDoS**: Firewall and IAM policies to limit traffic and control privileges.

### Advanced Features
- Disaster recovery databases hosted in secure data centers.
- Automated incident response with real-time alerts.

---

## Setup and Installation

### Prerequisites
- AWS account with EC2, VPC, and IAM permissions.
- Python 3.8+ installed on the local machine.
- OpenVPN setup on a server instance.

---

## Results and Analysis

- **Data Security**: All traffic between IIoT devices and servers is encrypted, ensuring data confidentiality.
- **Access Control**: Only authorized VPN users can access the SSH server.
- **Threat Detection**: CloudWatch metrics and email alerts provide proactive threat response.
- **Performance**: The system efficiently handles high volumes of data with minimal latency.

---

## Future Scope

1. **Machine Learning Integration**:
   - Use anomaly detection to identify advanced threats.
2. **Zero Trust Architecture**:
   - Enforce strict verification for every access request.
3. **Scalable Deployments**:
   - Extend the solution to hybrid and multi-cloud environments.

---

## References

1. [AWS Documentation](https://aws.amazon.com/documentation/)
2. "Virtual Private Networks (VPNs) for Industrial IoT Security" by J. Kim et al. (2023)
3. "Enhancing IIoT Security with Secure Shell (SSH)" by R. Gupta et al. (2022)

For a complete list, refer to the `References` section in the project report.
