from django.db import models

STATUS_ASSET = (
    ('operational', 'OPERATIONAL'),
    ('need_upgrade', 'NEEDS UPGRADE'),
    ('faulty', 'FAULTY'),
    ('retrieved', 'RETRIEVED')

)
STATUS_ASSET_LOCATION = (
    ('adeniyi_jones', 'ADENIYI JONES'),
    ('ogudu', 'OGUDU'),
    ('ipaja', 'IPAJA'),
    ('lasuth', 'LASUTH'),
    ('mcc', 'MCC'),
    ('vedic', 'VEDIC')

)

STATUS_ASSET_SUB_LOCATION = (
    ('mss_accounts', 'ACCOUNTS'),
    ('mss_bids_and_commercial', 'BIDS & COMMERCIAL'),
    ('mss_engineering', 'BIOMEDICAL ENGINEERING'),
    ('logistic', 'DISPATCH AND DRIVERS'),
    ('mss_emerging_business', 'EMERGING BUSINESS'),
    ('facility', 'FACILITY'),
    ('front_desk', 'FRONT DESK'),
    ('hr', 'HUMAN RESOURCES'),
    ('hmo', 'HMO'),
    ('inventory', 'INVENTORY'),
    ('mss_lab', 'MSS LAB'),
    ('pharmacy', 'PHARMACY'),
    ('social_media', 'SOCIAL MEDIA'),
    ('mss_projects', 'SPECIAL PROJECTS'),
    ('mss_sales', 'STRATEGIC SALES')

)

STATUS_EMAIL = (
    ('deleted', 'DELETED'),
    ('functional', 'FUNCTIONAL'),
    ('suspended', 'SUSPENDED')

)


class Inventories(models.Model):
    asset_id = models.IntegerField()
    asset_user = models.CharField(max_length=255)
    asset_vendor = models.CharField(max_length=255)
    asset_status = models.CharField(max_length=16, choices=STATUS_ASSET, default='operational')
    asset_name = models.CharField(max_length=255)
    asset_desc = models.TextField()
    asset_model = models.CharField(max_length=255)
    asset_image_url = models.URLField(max_length=2083)
    next_maintenance = models.DateField()
    asset_location = models.CharField(max_length=16, choices=STATUS_ASSET_LOCATION, default='ogudu')
    asset_sub_location = models.CharField(max_length=32, choices=STATUS_ASSET_SUB_LOCATION, default='mss_accounts')
    asset_serial_no = models.CharField(max_length=32)



class Department(models.Model):
    department_id = models.IntegerField()
    department_name = models.TextField()
    department_assets = models.TextField()


class Email(models.Model):
    staff_name = models.TextField(max_length=255)
    staff_email = models.EmailField()
    staff_password = models.TextField()
    staff_email_status = models.CharField(max_length=16, choices=STATUS_EMAIL, default='functional')


class Assigned_Gadget(models.Model):
    staff = models.CharField(max_length=255)
    gadget = models.TextField()
