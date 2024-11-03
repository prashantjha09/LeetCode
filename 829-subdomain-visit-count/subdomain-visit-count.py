class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_hit_frequency = defaultdict(int)
        for i in range(len(cpdomains)):
            hit_count = cpdomains[i].split(" ")[0]
            domain_name = cpdomains[i].split(" ")[1].split(".")
            domain_length = len(domain_name)
            domain_hit_frequency[cpdomains[i].split(" ")[1]] += int(hit_count)
            if domain_length == 3:
                domain_hit_frequency[domain_name[domain_length-2]+"."+domain_name[domain_length-1]] += int(hit_count)
            domain_hit_frequency[domain_name[domain_length-1]] += int(hit_count)

        return [f'{domain_hit_frequency[domain_call]} {domain_call}' for domain_call in domain_hit_frequency]
