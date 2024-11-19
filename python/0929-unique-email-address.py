class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def getemail(email):
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            return local +"@"+ domain
        
        hash_set = set()
        for email in emails:
                hash_set.add(getemail(email))
        
        return len(hash_set)