# Meraki --- Phase 1 Goals

## 1. Phase 1 Objective

Develop a Minimum Viable Product (MVP) of Meraki as a lightweight,
modular Python backend framework that can be packaged and distributed as
a pip-installable package.

The framework will provide the core backend infrastructure required to
build Python web applications, while keeping the core lightweight and
allowing additional functionality to be introduced through
extensions/plugins.

## 2. Distribution

-   Configure Meraki as a standard Python package using
    `pyproject.toml`.
-   Ensure the package can be installed using `pip`.
-   Prepare the project structure for future distribution through PyPI.
-   Keep framework dependencies minimal.

## 3. HTTP / ASGI Layer

-   Use an ASGI-compatible architecture for the framework.
-   Use Uvicorn as the underlying ASGI server.
-   Establish a clear boundary between Meraki and the underlying server.
-   Provide framework-level request and response abstractions rather
    than exposing server-specific details to application code.

## 4. Application Core

-   Provide a central application object responsible for coordinating
    the framework.
-   Establish the application lifecycle.
-   Provide startup and shutdown handling.
-   Integrate routing, middleware, configuration, and plugins through
    the application core.

## 5. Request and Response Handling

-   Define standardized request and response abstractions.
-   Provide access to relevant HTTP request information.
-   Provide a consistent mechanism for creating HTTP responses.
-   Keep request/response handling independent from the underlying ASGI
    server implementation.

## 6. Routing

-   Provide a route registration mechanism.
-   Support standard HTTP methods.
-   Map incoming requests to registered application handlers.
-   Support path-based route matching.
-   Provide appropriate handling for unmatched routes.

## 7. Middleware

-   Provide a middleware registration mechanism.
-   Implement a request-processing pipeline.
-   Allow middleware to process requests before route handlers.
-   Allow middleware to process responses after route handlers.
-   Keep middleware independent and composable.

## 8. Plugin Architecture

-   Define a common plugin interface.
-   Provide a plugin manager responsible for managing registered
    plugins.
-   Support plugin initialization and lifecycle integration.
-   Allow plugins to extend framework functionality without modifying
    the core.
-   Establish the foundation for independently developed extensions.

## 9. Configuration

-   Provide a centralized configuration mechanism.
-   Allow framework settings to be configured consistently.
-   Support configuration required by the application and extensions.
-   Keep configuration independent from individual framework components.

## 10. Error Handling

-   Define common framework exceptions.
-   Provide a consistent mechanism for handling framework-level errors.
-   Ensure errors can be translated into appropriate HTTP responses
    where applicable.
-   Keep error handling centralized and extensible.

## 11. Database Extension

Phase 1 will establish database support as the first concrete extension
of the Meraki architecture.

### 11.1 Database Abstraction

-   Define a common `DatabaseConnector` interface.
-   Establish common operations required by supported SQL databases.
-   Keep the framework independent of database-specific implementations.
-   Use the Strategy Pattern to allow database implementations to be
    interchangeable.

### 11.2 Initial Database Implementations

The initial database extension will target:

-   PostgreSQL
-   MySQL
-   SQLite
-   SQL Server

Each implementation will conform to the common database connector
interface while handling database-specific driver integration and
behavior.

## 12. Testing

-   Establish a test structure corresponding to the framework modules.
-   Add tests for the core application lifecycle.
-   Add tests for routing.
-   Add tests for middleware behavior.
-   Add tests for plugin registration and management.
-   Add tests for database connector behavior and implementations.
-   Ensure new extensions can be tested independently.

## 13. Documentation

-   Document the core architecture and project structure.
-   Document the MVP usage flow.
-   Document the plugin architecture.
-   Document the database connector interface.
-   Provide a minimal example demonstrating how to create and run a
    Meraki application.

## 14. Phase 1 Completion Criteria

Phase 1 will be considered complete when:

-   Meraki can be installed as a Python package.
-   A basic Meraki application can be created and started.
-   Uvicorn can serve the application through the ASGI interface.
-   Requests can be routed to application handlers.
-   Middleware can participate in the request/response pipeline.
-   Plugins can be registered and integrated with the application
    lifecycle.
-   Configuration and framework-level error handling are available.
-   The database extension has a defined common interface.
-   The initial SQL database implementations conform to that interface.
-   Core functionality is covered by tests.
-   A basic working example and developer documentation are available.

## 15. Out of Scope for Phase 1

The following are not part of the Phase 1 MVP unless explicitly added
later:

-   Additional framework features beyond the defined core requirements
-   Advanced database abstractions such as a full ORM
-   Database-specific features that cannot be represented by the common
    connector abstraction
-   Additional extensions not required to validate the plugin
    architecture
-   Production-scale optimization and advanced deployment tooling
