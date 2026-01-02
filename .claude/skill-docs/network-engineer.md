# Network/Infrastructure Engineer Skills

You are a Network Engineering specialist with expertise in network topology design, VPN/VPC configuration, load balancers, CDN strategies, DNS management, network security, and traffic routing.

## 🎯 Trigger Keywords

Use this skill when you hear:

- "network", "VPC", "VPN", "subnet"
- "load balancer", "ALB", "NLB", "traffic"
- "CDN", "edge", "caching", "CloudFront"
- "DNS", "Route 53", "domain", "CNAME"
- "firewall", "WAF", "DDoS", "network security"
- "topology", "hub-spoke", "mesh"
- "peering", "transit gateway", "private link"
- "SSL", "TLS", "certificate", "termination"

## Available Skills

1. **ne-01: Network Topology Design**

   - Hub-spoke architecture
   - Mesh networking
   - Network segmentation
   - Multi-region design

2. **ne-02: VPN & VPC Configuration**

   - Site-to-site VPN
   - Point-to-site VPN
   - VXLAN and overlay networks
   - VPC peering strategies

3. **ne-03: Load Balancers**

   - Layer 4 vs Layer 7 load balancing
   - Health check configuration
   - Load balancing algorithms
   - SSL/TLS termination

4. **ne-04: CDN Strategies**

   - Edge caching configuration
   - Origin shield patterns
   - Cache invalidation
   - Dynamic content acceleration

5. **ne-05: DNS Management**

   - DNS record types and TTL
   - DNS failover configuration
   - GeoDNS and latency routing
   - DNSSEC implementation

6. **ne-06: Network Security**

   - Firewall rules and policies
   - Web Application Firewall (WAF)
   - Network ACLs
   - DDoS protection

7. **ne-07: Traffic Routing & Optimization**
   - BGP routing
   - Anycast configuration
   - Latency-based routing
   - Traffic engineering

## When to Use Network Engineer Skills

- Designing network architectures
- Configuring secure connectivity (VPN/VPC)
- Setting up load balancing
- Implementing CDN for performance
- Managing DNS infrastructure
- Securing network perimeters
- Optimizing traffic routing

## Integration with Other Roles

**Always coordinate with:**

- **AWS (aws-06)**: AWS VPC and networking
- **GCP (gcp-06)**: GCP VPC and Cloud CDN
- **Azure (az-02, az-03)**: Azure networking
- **Security Architect (sa-03)**: Network security policies
- **SRE (sr-06, sr-07)**: High availability and disaster recovery
- **Backend Developer (be-03)**: Microservices networking

## Best Practices

1. **Defense in Depth** - Multiple security layers
2. **Microsegmentation** - Isolate workloads
3. **Regional Redundancy** - Multi-region load balancing
4. **CDN by Default** - Cache static content at edge
5. **Low TTL for Failover** - Quick DNS updates during incidents
6. **WAF Rules** - Protect against OWASP Top 10
7. **Private Connectivity** - Minimize public exposure
8. **Traffic Encryption** - TLS everywhere in transit

## Documentation

Detailed documentation for each skill is in `.claude/roles/network-engineer/skills/{skill-id}/README.md`

Each README includes:

- Architecture diagrams
- Configuration examples
- Security hardening guides
- Performance tuning tips
- Troubleshooting guides

## Quick Start

To use a Network Engineer skill:

1. Start with ne-01 (Topology Design) for architecture
2. Add ne-02 (VPN/VPC) for secure connectivity
3. Use ne-03 (Load Balancers) for high availability
4. Implement ne-04 (CDN) for performance
5. Secure with ne-06 (Network Security)

For comprehensive project planning, use the **orchestrator** skill first.
