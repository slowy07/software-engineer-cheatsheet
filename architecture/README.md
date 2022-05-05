# architecture

- [architecture](#architecture)
  - [what is software architecture](#what-is-software-architecture)
  - [modular elements (modules)](#modular-elements-modules)
  - [understanding the problem, functional requirements (solve a valid bussines problem or have recognizable return on investment)](#understanding-the-problem-functional-requirements-solve-a-valid-bussines-problem-or-have-recognizable-return-on-investment)
  - [Evaluate the architecture design (non functional requirements, quality attributes, constraints)](#evaluate-the-architecture-design-non-functional-requirements-quality-attributes-constraints)
  - [good architecture principles](#good-architecture-principles)
  - [separation of concerns](#separation-of-concerns)
  - [SOLID](#solid)

## what is software architecture

Software architecture refers to the fundamental structures of a software system and the discipline of creating such structures and systems. Each structure comprises software elements, relations among them, and properties of both elements and relations. The architecture of a software system is a metaphor, analogous to the architecture of a building. It functions as a blueprint for the system and the developing project, laying out the tasks necessary to be executed by the design teams.


Software architecture is about making fundamental structural choices that are costly to change once implemented. Software architecture choices include specific structural options from possibilities in the design of the software. For example, the systems that controlled the Space Shuttle launch vehicle had the requirement of being very fast and very reliable. Therefore, an appropriate real-time computing language would need to be chosen. Additionally, to satisfy the need for reliability the choice could be made to have multiple redundant and independently produced copies of the program, and to run these copies on independent hardware while cross-checking results.


[software architecture design tools](https://www.castsoftware.com/glossary/what-is-software-architecture-tools-design-definition-explanation-best)

## modular elements (modules)

[Modular Software architectures](https://www.tutisani.com/software-architecture/modular-software-architecture.html)

## understanding the problem, functional requirements (solve a valid bussines problem or have recognizable return on investment)

Functional Requirement (FR) is a description of the service that the software must offer. It describes a software system or its component. A function is nothing but inputs to the software system, its behavior, and outputs. It can be a calculation, data manipulation, business process, user interaction, or any other specific functionality which defines what function a system is likely to perform. Functional Requirements in Software Engineering are also called Functional Specification.

In software engineering and systems engineering, a Functional Requirement can range from the high-level abstract statement of the sender’s necessity to detailed mathematical functional requirement specifications. Functional software requirements help you to capture the intended behaviour of the system.


[More information](https://www.guru99.com/functional-requirement-specification-example.html)

## Evaluate the architecture design (non functional requirements, quality attributes, constraints)

Nonfunctional Requirements (NFRs) define system attributes such as security, reliability, performance, maintainability, scalability, and usability. They serve as constraints or restrictions on the design of the system across the different backlogs. Also known as system qualities, nonfunctional requirements are just as critical as functional Epics, Capabilities, Features, and Stories. They ensure the usability and effectiveness of the entire system. Failing to meet any one of them can result in systems that fail to satisfy internal business, user, or market needs, or that do not fulfill mandatory requirements imposed by regulatory or standards agencies.  In some cases, non-compliance can cause significant legal issues (privacy, security, safety, to name a few).


**Details**

Functional requirements expressed in user stories, features, and capabilities represent most of the work in building solutions that deliver value to the user. Although they may be a bit subtler, NFRs are just as important to system success as they describe critical operational qualities required for release (or manufacture, or sell). NFRs are not themselves backlog items. They are constraints on development that limit some degree of design freedom for those building the system. These constraints are often defined in the acceptance criteria for multiple backlog items. For example, SAML-based Single Sign-on (SSO) is a requirement for all products in the suite. SSO is a functional requirement, while SAML is a constraint. And any backlog item building sign-on functionality would reference the SAML constraint in its acceptance criteria. ‘FURPS’ is a commonly referenced set of important quality attributes: Functionality, Usability, Reliability, Performance, and Supportability. The NFR list is more exhaustive and includes compliance, security, resilience, privacy, accessibility, and others.

## good architecture principles

Architecture lays out a firm foundation for any software project. A sound architecture defines the technical standards, design, delivery, and support framework of the software product. While designing software architecture, one should keep in mind the development and technology goals and ensure everything is logical, scalable, and cost-efficient.

Solutions architects play a significant role in designing system architecture, with an understanding of technical standards like platforms, technologies, and infrastructure. Their analysis directly helps to successfully define the product, perfect the design, and provide on-time, cost-efficient delivery and lifetime support. Therefore, they have to understand the technology goals of the organization along with the client’s business needs.

To make a software project successful, software architects must follow a set of basic rules, guidelines, and principles. These are the three key principles of software architecture that you should never forget.

[What software architecture makes it good](https://www.codementor.io/learn-development/what-makes-good-software-architecture-101)


## separation of concerns

In computer science, separation of concerns (SoC) is a design principle for separating a computer program into distinct sections. Each section addresses a separate concern, a set of information that affects the code of a computer program. A concern can be as general as "the details of the hardware for an application", or as specific as "the name of which class to instantiate". A program that embodies SoC well is called a modular program. Modularity, and hence separation of concerns, is achieved by encapsulating information inside a section of code that has a well-defined interface. Encapsulation is a means of information hiding. Layered designs in information systems are another embodiment of separation of concerns (e.g., presentation layer, business logic layer, data access layer, persistence layer).


Separation of concerns results in more degrees of freedom for some aspect of the program's design, deployment, or usage. Common among these is increased freedom for simplification and maintenance of code. When concerns are well-separated, there are more opportunities for module upgrade, reuse, and independent development. Hiding the implementation details of modules behind an interface enables improving or modifying a single concern's section of code without having to know the details of other sections and without having to make corresponding changes to those other sections. Modules can also expose different versions of an interface, which increases the freedom to upgrade a complex system in piecemeal fashion without interim loss of functionality.


Separation of concerns is a form of abstraction. As with most abstractions, separating concerns means adding additional code interfaces, generally creating more code to be executed. So despite the many benefits of well-separated concerns, there is often an associated execution penalty.


**Implementation**


The mechanisms for modular or object-oriented programming that are provided by a programming language are mechanisms that allow developers to provide SoC. For example, object-oriented programming languages such as C#, C++, Delphi, and Java can separate concerns into objects, and architectural design patterns like MVC or MVP can separate content from presentation and the data-processing (model) from content. Service-oriented design can separate concerns into services. Procedural programming languages such as C and Pascal can separate concerns into procedures or functions. Aspect-oriented programming languages can separate concerns into aspects and objects.

Separation of concerns is an important design principle in many other areas as well, such as urban planning, architecture and information design. The goal is to more effectively understand, design, and manage complex interdependent systems, so that functions can be reused, optimized independently of other functions, and insulated from the potential failure of other functions.

Common examples include separating a space into rooms, so that activity in one room does not affect people in other rooms, and keeping the stove on one circuit and the lights on another, so that overload by the stove does not turn the lights off. The example with rooms shows encapsulation, where information inside one room, such as how messy it is, is not available to the other rooms, except through the interface, which is the door. The example with circuits demonstrates that activity inside one module, which is a circuit with consumers of electricity attached, does not affect activity in a different module, so each module is not concerned with what happens in the other.


## SOLID

In software engineering, SOLID is a mnemonic acronym for five design principles intended to make software designs more understandable, flexible, and maintainable. The principles are a subset of many principles promoted by American software engineer and instructor Robert C. Martin, first introduced in his 2000 paper Design Principles and Design Patterns. The SOLID ideas are

- The single-responsibility principle: "There should never be more than one reason for a class to change." In other words, every class should have only one responsibility.
- The open–closed principle: "Software entities ... should be open for extension, but closed for modification."
- The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."
- The interface segregation principle: "Many client-specific interfaces are better than one general-purpose interface."
- The dependency inversion principle: "Depend upon abstractions, __[not]__ concretions."

