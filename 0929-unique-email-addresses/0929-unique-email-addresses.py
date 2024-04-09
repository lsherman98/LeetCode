class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        
        for email in emails:
            email = email.split('@')
            local = email[0]
            domain = email[1]
            clean = self.clean_email(local) + '@' + domain
            if clean not in result:
                result.append(clean)
                
        return len(result)
            
    
    
    def clean_email(self, email):
        new_email = ''
        for c in email:
            if c == '.':
                continue
            if c == '+':
                break
            new_email += c
        return new_email
            
        