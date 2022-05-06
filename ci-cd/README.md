# CI-CD

- [CI-CD](#ci-cd)
  - [What it is](#what-it-is)
  - [CI vs CDelivery vs CDeployment](#ci-vs-cdelivery-vs-cdeployment)
  - [Setup CI/CD on the next ideal project](#setup-cicd-on-the-next-ideal-project)

## What it is

It used to be that software development was simply about, well, software development. As software continues to eat the world, many adjacent aspects of the development process have become ripe for code to take over. Infrastructure topics such as integration and deployment are prime examples. This explains the rise of DevOps. And within DevOps, the CI/CD pipeline is now mainstream among software companies.


If you’re in IT leadership, understanding the CI/CD pipeline is critical to keeping your organization on par with other software companies. That’s why, in this article, I’m going to dive into what you need to know: the concepts of CI/CD, what the CI/CD pipeline is, and why it matters.

**Important of CI/CD**


Both CI and CD form the backbone of the modern DevOps environment. You can think of CI/CD processes as similar to a software development lifecycle. Nowadays, the concept of CI/CD is everywhere. Just take a look at the February 2019 trends report by InfoQ on DevOps topics. In it, I count no less than four topics on CI/CD in the early and late majority. There’s even a fifth topic regarding the use of code vs. config in the CD pipeline.

In other words, the importance of CI/CD is no longer in question. When the community talks about CI/CD and the cutting edge in the same sentence, usually it’s about the implementation details of the CI/CD pipeline.


**Continuous integration**


Continuous Integration (CI) is a development practice that requires developers to integrate code into a shared repository several times a day. Each check-in is then verified by an automated build, allowing teams to detect problems early.


The key details to note are that you need to run code integration multiple times a day, every day, and you need to run the automated verification of the integration. What’s the motivation for this? Well, in the development process, the earlier we surface errors, the better. And one source of frequently occurring errors is the code integration step.


When you have a team of developers, each of whom is responsible for a separate feature, you need to integrate the different features before you’re ready for a release. By integrating so frequently, your team can surface errors earlier. And when those are caught, the amount of backtracking needed to find the cause is also much reduced. Therefore, your team can resolve the integration errors much faster.


**Continuous deployment**


Continuous Deployment is closely related to Continuous Integration and refers to the release into production of software that passes the automated tests.


So why do you need to care about continuous deployment as part of your development process? Well, when there are releases, there will be deployment steps. These deployment steps tend to repeat for each release. Instead of performing the deployment manually for each release, why not have the deployment steps be executed automatically? Of course, ideally, this code has been built and tested successfully by the CI server too.

## CI vs CDelivery vs CDeployment

[Continuous inegration vs continuous delivery vs continuous deployment](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)

## Setup CI/CD on the next ideal project

[An introduction to CI/CD best practices | digital ocean](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)