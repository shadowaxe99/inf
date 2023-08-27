```python
import os
from gdpr import GDPR
from ccpa import CCPA

class ComplianceMonitor:
    def __init__(self):
        self.gdpr = GDPR()
        self.ccpa = CCPA()

    def monitor_compliance(self, user_data):
        if user_data['region'] == 'EU':
            return self.gdpr.check_compliance(user_data)
        elif user_data['region'] == 'California':
            return self.ccpa.check_compliance(user_data)
        else:
            return True

    def handle_non_compliance(self, user_data):
        if user_data['region'] == 'EU':
            self.gdpr.handle_non_compliance(user_data)
        elif user_data['region'] == 'California':
            self.ccpa.handle_non_compliance(user_data)

if __name__ == "__main__":
    compliance_monitor = ComplianceMonitor()
    user_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com',
        'region': 'EU',
        'data_processing_consent': False
    }
    if not compliance_monitor.monitor_compliance(user_data):
        compliance_monitor.handle_non_compliance(user_data)
```