ibmcloud ce project current

ibmcloud ce project get --name 'Code Engine - sn-labs-cnshirui'


===

theia@theiadocker-cnshirui:/home/project/final_project/myapp$ ibmcloud ce project current
Getting the current project context...
OK

Name:       Code Engine - sn-labs-cnshirui  
ID:         f99b4941-121d-4e30-afb7-171b24cd33fc  
Subdomain:  1yb03hmeylk7  
Domain:     us-south.codeengine.appdomain.cloud  
Region:     us-south  

Kubernetes Config:    
Context:               1yb03hmeylk7  
Environment Variable:  export KUBECONFIG="/home/theia/.bluemix/plugins/code-engine/Code Engine - sn-labs-cnshirui-f99b4941-121d-4e30-afb7-171b24cd33fc.yaml"  
theia@theiadocker-cnshirui:/home/project/final_project/myapp$ ibmcloud ce project get --name 'Code Engine - sn-labs-cnshirui'
Getting project 'Code Engine - sn-labs-cnshirui'...
OK

Name:                                      Code Engine - sn-labs-cnshirui  
ID:                                        f99b4941-121d-4e30-afb7-171b24cd33fc  
CRN:                                       crn:v1:bluemix:public:codeengine:us-south:a/f672382e1b43496b83f7a82fd31a59e8:f99b4941-121d-4e30-afb7-171b24cd33fc::  
Status:                                    active  
Enabled:                                   true  
Application Private Visibility Supported:  true  
Selected:                                  true  
Tags:                                      cnshirui,skillsnetwork  
Region:                                    us-south  
Resource Group:                            production  
Service Binding Service ID:                Project not configured for service binding  
Age:                                       6h35m  
Created:                                   Sat, 26 Jul 2025 01:40:59 -0400  
Updated:                                   Sat, 26 Jul 2025 01:42:58 -0400  

Outbound IP addresses:    
  Public Internet  
  52.118.190.143  
  169.47.92.216  
  52.117.4.162  
  
  IBM Cloud private network  
  10.249.194.148  
  10.22.27.96  
  10.22.39.94  

Quotas:                   
  Category                                  Used  Limit  
  App revisions                             0     120  
  Apps                                      0     40  
  Build runs                                0     100  
  Builds                                    1     100  
  Configmaps                                2     100  
  CPU                                       0     6  
  Custom domain mappings                    0     80  
  Ephemeral storage                         0     20G  
  Functions                                 0     20  
  Instances (active)                        0     250  
  Instances (total)                         0     2500  
  Job runs                                  0     100  
  Jobs                                      0     100  
  Memory                                    0     20G  
  Secrets                                   5     100  
  Subscriptions (cron)                      0     100  
  Subscriptions (IBM Cloud Object Storage)  0     100  
  Subscriptions (Kafka)                     0     100  