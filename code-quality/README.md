## what is code quality

Code that checks your spelling while writing a document is not very critical compared to code that runs your implantable cardioverter-defibrillator in treatment for sudden cardiac death due to ventricular tachyarrhythmias. Yet, most will be consistent with the contention that error-free code which reliably performs its intended function defines code quality. The maintainability of functionality is critical regardless.

However, there are other properties to code that contribute to high-quality code that should not be omitted from this equation. These include code maintainability, clarity, testability, portability, robustness, reusability, complexity, safety, security, and more.

These code quality metrics can determine how a single piece of code might affect the overall quality of your code. Code review tools offer one more vector toward avoiding low-quality code, time-consuming fixes, and the other common pitfalls developer teams face during software development. Knowing what makes quality code is just as important as knowing how to measure code quality.


**Why code quality matters**


The code quality is important, as it impacts the overall software quality. And quality impacts how safe, secure, and reliable your codebase is.

High quality is critical for many development teams today. And it's especially important for those developing safety-critical systems.


**Code quality analysis: Good code vs bad code**


Good code is high quality. And it’s clean code. It stands the test of time. Bad code is low quality. It won’t last long.

Essentially, code that is considered good:

- does what it should.
- follows a consistent style.
- it is easy to understand.
- has been well-documented
- it can be tested


**How to measure code quality**

There’s no one way to measure the quality of your code. What you measure may be different from what other development team measures.

__realibility__


Reliability measures the probability that a system will run without failure over a specific period of operation. It relates to the number of defects and availability of the software.

Reliability measures the probability that a system will run without failure over a specific period of operation. It relates to the number of defects and availability of the software.


__maintainaability__


Maintainability measures how easily software can be maintained. It relates to the size, consistency, structure, and complexity of the codebase. And ensuring maintainable source code relies on a number of factors, such as testability and understandability.

You can’t use a single metric to ensure maintainability. Some metrics you may consider to improve maintainability are the number of stylistic warnings and Halstead complexity measures. Both automation and human reviewers are essential for developing maintainable codebases.


__testability__


Testability measures how well the software supports testing efforts. It relies on how well you can control, observe, isolate, and automate testing, among other factors.

Testability can be measured based on how many test cases you need to find potential faults in the system. Size and complexity of the software can impact testability. So, applying methods at the code level — such as cyclomatic complexity — can help you improve the testability of the component.


__portability__


Testability measures how well the software supports testing efforts. It relies on how well you can control, observe, isolate, and automate testing, among other factors.

Testability can be measured based on how many test cases you need to find potential faults in the system. Size and complexity of the software can impact testability. So, applying methods at the code level — such as cyclomatic complexity — can help you improve the testability of the component.


__reusability__


Reusability measures whether existing assets — such as code — can be used again. Assets are more easily reused if they have characteristics such as modularity or loose coupling.

Reusability can be measured by the number of interdependencies. Running a static analyzer can help you identify these interdependencies.


## Test pyramid (all types of test)

[The practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)

## Unit testing vs intergration testing vs E2E testing

[Static vs Unit vs Integration vs E2E testing for fronted apps](https://kentcdodds.com/blog/static-vs-unit-vs-integration-vs-e2e-tests)

## code should be covered with unit test


**What should test?**
- Test the common case of everything you can. this wil tell you when that code breaks after you make some change (which is, in my opinion, the single greaatest benefit of automated unit testing).
- test the edge cases of a few unusually complex code that you think will probably have errors.
- whenever you find a bug, write a test case to cover it before fixing it
- add edge-case test to less critical code whenever someone has time to kill.

**what sould not test?**
- the code is trivial. A getter that ``return 0`` doesn't need to be tested, and changes will be recovered by test for its consumers.
- the code simply passes trough into a stable API. i'll assume thaat the standard libary works properly
- the code needs to interact ith other deployed system; then an integration test is called for.
- if the test of succes/fail is something that is so difficult to quantify as to not be reliably measureable, such as stenography being unnoticeable humans.
- if the test itself is an order of magnitude more difficult to write than the code.
- if the code is throw-away or placeholder code. if there's any doubt, test.

## TDD explanation

Test Driven Development (TDD) is software development approach in which test cases are developed to specify and validate what the code will do. In simple terms, test cases for each functionality are created and tested first and if the test fails then the new code is written in order to pass the test and making code simple and bug-free.

Test-Driven Development starts with designing and developing tests for every small functionality of an application. TDD framework instructs developers to write new code only if an automated test has failed. This avoids duplication of code. The TDD full form is Test-driven development.

The simple concept of TDD is to write and correct the failed tests before writing new code (before development). This helps to avoid duplication of code as we write a small amount of code at a time in order to pass tests. (Tests are nothing but requirement conditions that we need to test to fulfill them).

Test-Driven development is a process of developing and running automated test before actual development of the application. Hence, TDD sometimes also called as Test First Development.


**perform TDD test**

- add test
- run all test nd see if any new test fails.
- write some code
- run test and refactor code
- repeat

## Code quality metrics

[Code quality metrics](https://se-education.org/learningresources/contents/codeQuality/CodeQualityMetrics.html)

## keep secure

[Code quality and code security | SonarQube](https://www.sonarqube.org/)
