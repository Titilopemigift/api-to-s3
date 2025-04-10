<!-- ARN FORMAT/PATTERN -->

1.	S3 accesspoint: arn:${Partition}:s3:${Region}:${Account}:accesspoint/${AccessPointName}
Link: https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html

2.	S3 bucket: arn:${Partition}:s3:::${BucketName}
Link: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html

3.	S3 storagelensgroup: arn:${Partition}:s3:${Region}:${Account}:storage-lens-group/${Name}
Link: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_group.html

4.	S3 object: arn:${Partition}:s3:::${BucketName}/${ObjectName}
Link: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingObjects.html

5.	IAM mfa: arn:${Partition}:iam::${Account}:mfa/${MfaTokenIdWithPath}
Link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html

6.	IAM role: arn:${Partition}:iam::${Account}:role/${RoleNameWithPath}
Link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html

7.	IAM user: arn:${Partition}:iam::${Account}:user/${UserNameWithPath}
Link: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html

8.	EC2 elastic-ip: arn:${Partition}:ec2:${Region}:${Account}:elastic-ip/${AllocationId}
Link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html

9.	EC2 fleet: arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}
Link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html

10.	EC2 instance: arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}
Link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Instances.html

11.	EC2  image: arn:${Partition}:ec2:${Region}::image/${ImageId}
Link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html



