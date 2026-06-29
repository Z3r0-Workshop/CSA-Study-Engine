# Hand-written CSA question bank — source="seed"
# Weights match the official ServiceNow CSA exam blueprint percentages.

TOPICS = [
    {
        "name": "User Interface & Navigation",
        "weight": 0.14,
        "blueprint_notes": (
            "Application Navigator, Banner frame, Content frame, "
            "Favorites, History, Forms, Lists, Field types, Breadcrumbs"
        ),
    },
    {
        "name": "Collaboration",
        "weight": 0.13,
        "blueprint_notes": (
            "Work Notes, Additional Comments, Watch List, "
            "Connect Chat, Activity Stream, Notifications"
        ),
    },
    {
        "name": "Self-Service & Automation",
        "weight": 0.13,
        "blueprint_notes": (
            "Service Portal, Knowledge Base, Virtual Agent, "
            "Predictive Intelligence, Subscriptions"
        ),
    },
    {
        "name": "Database Management",
        "weight": 0.11,
        "blueprint_notes": (
            "Tables, Records, Fields, Table inheritance, "
            "Schema Map, Application Files, Import Sets"
        ),
    },
    {
        "name": "Workflow & Automation",
        "weight": 0.11,
        "blueprint_notes": (
            "Flow Designer, Business Rules, Script Includes, "
            "Scheduled Jobs, Approvals, Subflows"
        ),
    },
    {
        "name": "Application & Module Development",
        "weight": 0.11,
        "blueprint_notes": (
            "Studio, Scoped vs Global apps, Application Menus, "
            "Modules, Update Sets, Application scope"
        ),
    },
    {
        "name": "Reporting",
        "weight": 0.09,
        "blueprint_notes": (
            "Report types, Dashboards, Performance Analytics, "
            "Scheduled reports, Gauges, Report sharing"
        ),
    },
    {
        "name": "Service Catalog",
        "weight": 0.09,
        "blueprint_notes": (
            "Catalog Items, Variables, Order Guides, Record Producers, "
            "Catalog Client Scripts, Catalog UI Policies, Workflows"
        ),
    },
    {
        "name": "CMDB",
        "weight": 0.09,
        "blueprint_notes": (
            "Configuration Items, CI classes, Discovery, "
            "CI Relationships, CI Lifecycle, CMDB Health"
        ),
    },
]

QUESTIONS = [
    # ── User Interface & Navigation ──────────────────────────────────────────
    {
        "topic": "User Interface & Navigation",
        "stem": "Which part of the ServiceNow UI is used to find and navigate to applications and modules?",
        "kind": "mcq",
        "options": [
            "Application Navigator",
            "Content Frame",
            "Banner Frame",
            "Service Portal",
        ],
        "answer": "Application Navigator",
        "explanation": (
            "The Application Navigator is the left-side panel that lists all installed "
            "applications and their modules, allowing users to navigate the platform."
        ),
    },
    {
        "topic": "User Interface & Navigation",
        "stem": "What does clicking the star icon next to a module in the Application Navigator do?",
        "kind": "mcq",
        "options": [
            "Marks it as a favorite for quick access",
            "Marks it as urgent",
            "Opens the record in a new tab",
            "Adds it to the dashboard",
        ],
        "answer": "Marks it as a favorite for quick access",
        "explanation": (
            "Starring a module adds it to the Favorites section at the top of the "
            "Application Navigator so you can reach it without searching."
        ),
    },
    {
        "topic": "User Interface & Navigation",
        "stem": "What is the purpose of the Filter Navigator text field at the top of the Application Navigator?",
        "kind": "mcq",
        "options": [
            "Filters the list of applications and modules visible in the navigator",
            "Searches all records across the entire instance",
            "Filters rows in the currently open list view",
            "Creates a saved filter condition on a table",
        ],
        "answer": "Filters the list of applications and modules visible in the navigator",
        "explanation": (
            "Typing in the Filter Navigator instantly narrows the app/module list, "
            "making it easy to jump to any module without scrolling."
        ),
    },
    # ── Collaboration ────────────────────────────────────────────────────────
    {
        "topic": "Collaboration",
        "stem": "Which journal field on a ServiceNow record is visible to the end user (customer)?",
        "kind": "mcq",
        "options": [
            "Work Notes",
            "Additional Comments",
            "Internal Notes",
            "Agent Log",
        ],
        "answer": "Additional Comments",
        "explanation": (
            "Additional Comments are customer-visible and trigger notifications to the "
            "caller. Work Notes are internal and visible only to agents with the right role."
        ),
    },
    {
        "topic": "Collaboration",
        "stem": "What does adding a user to the Watch List on a record do?",
        "kind": "mcq",
        "options": [
            "Sends them email notifications when the record is updated",
            "Assigns them as the record owner",
            "Grants them edit rights to the record",
            "Subscribes them to a daily digest only",
        ],
        "answer": "Sends them email notifications when the record is updated",
        "explanation": (
            "Watch List users receive email notifications for changes to the record "
            "without being the assignee or a member of the assignment group."
        ),
    },
    {
        "topic": "Collaboration",
        "stem": "What is Connect Chat in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A real-time messaging tool built into the platform",
            "An API for integrating external chat systems",
            "A mobile-only communication feature",
            "A notification template builder for email alerts",
        ],
        "answer": "A real-time messaging tool built into the platform",
        "explanation": (
            "Connect Chat provides in-platform real-time messaging between users "
            "and can be associated with specific records for contextual collaboration."
        ),
    },
    # ── Self-Service & Automation ────────────────────────────────────────────
    {
        "topic": "Self-Service & Automation",
        "stem": "What is the primary purpose of the ServiceNow Service Portal?",
        "kind": "mcq",
        "options": [
            "To provide a consumer-style self-service interface for end users",
            "To manage ITSM workflows for IT agents",
            "To configure system properties and instance settings",
            "To build and run reports for managers",
        ],
        "answer": "To provide a consumer-style self-service interface for end users",
        "explanation": (
            "The Service Portal gives end users a modern, widget-based UI to submit "
            "requests, browse the knowledge base, and track their open tickets."
        ),
    },
    {
        "topic": "Self-Service & Automation",
        "stem": "Which ServiceNow capability uses machine learning to suggest resolutions based on similar historical incidents?",
        "kind": "mcq",
        "options": [
            "Predictive Intelligence",
            "Flow Designer",
            "Virtual Agent",
            "Performance Analytics",
        ],
        "answer": "Predictive Intelligence",
        "explanation": (
            "Predictive Intelligence applies ML models to automatically categorize, "
            "route, and suggest resolutions for incidents and cases."
        ),
    },
    {
        "topic": "Self-Service & Automation",
        "stem": "What is a Knowledge Base article in ServiceNow primarily used for?",
        "kind": "mcq",
        "options": [
            "Storing documented solutions so users can self-serve",
            "Tracking open and resolved incidents",
            "Defining approval steps for change requests",
            "Configuring variables on catalog items",
        ],
        "answer": "Storing documented solutions so users can self-serve",
        "explanation": (
            "Knowledge Base articles capture and share solutions, reducing repeat "
            "contacts to the service desk by letting users find answers themselves."
        ),
    },
    # ── Database Management ──────────────────────────────────────────────────
    {
        "topic": "Database Management",
        "stem": "In ServiceNow, what is a Table?",
        "kind": "mcq",
        "options": [
            "A collection of records of the same type stored in the database",
            "A UI widget that displays data in rows and columns on a form",
            "A configuration file that holds system property values",
            "A type of Flow Designer activity",
        ],
        "answer": "A collection of records of the same type stored in the database",
        "explanation": (
            "Every piece of data in ServiceNow lives in a table. "
            "For example, all incidents are stored in the Incident [incident] table."
        ),
    },
    {
        "topic": "Database Management",
        "stem": "What does table inheritance mean in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A child table inherits all fields and data from its parent table",
            "Records are automatically replicated between related tables",
            "A table imports its schema definition from an external CSV",
            "Views on a parent table apply automatically to all child tables",
        ],
        "answer": "A child table inherits all fields and data from its parent table",
        "explanation": (
            "When a table extends another, it inherits every column of the parent. "
            "The Incident table, for example, extends Task and gains all Task fields."
        ),
    },
    {
        "topic": "Database Management",
        "stem": "What is the Schema Map in ServiceNow used for?",
        "kind": "mcq",
        "options": [
            "Visualizing table relationships and inheritance hierarchies",
            "Mapping workflow states between environments",
            "Creating field-level mappings for data imports",
            "Configuring UI policies across related tables",
        ],
        "answer": "Visualizing table relationships and inheritance hierarchies",
        "explanation": (
            "The Schema Map is a graphical tool that shows how tables relate to and "
            "extend each other — useful for understanding data architecture at a glance."
        ),
    },
    # ── Workflow & Automation ────────────────────────────────────────────────
    {
        "topic": "Workflow & Automation",
        "stem": "What is Flow Designer in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A no-code/low-code tool for building automated process flows",
            "A drag-and-drop form layout editor",
            "A visual report configuration tool",
            "A tool for designing database table schemas",
        ],
        "answer": "A no-code/low-code tool for building automated process flows",
        "explanation": (
            "Flow Designer provides a natural-language interface to automate multi-step "
            "processes using triggers, actions, and conditions — no scripting required."
        ),
    },
    {
        "topic": "Workflow & Automation",
        "stem": "What is a Business Rule in ServiceNow?",
        "kind": "mcq",
        "options": [
            "Server-side JavaScript that runs when a record is inserted, updated, deleted, or queried",
            "A client-side script that validates field values before form submission",
            "A scheduled task that runs at a configured time interval",
            "An approval policy that enforces change management gates",
        ],
        "answer": "Server-side JavaScript that runs when a record is inserted, updated, deleted, or queried",
        "explanation": (
            "Business Rules run on the server and can modify records, send events, "
            "and enforce data integrity. They are scoped to a table and a trigger condition."
        ),
    },
    {
        "topic": "Workflow & Automation",
        "stem": "A 'before' Business Rule executes at which point in the save process?",
        "kind": "mcq",
        "options": [
            "Before the record is written to the database",
            "After the record is committed to the database",
            "Before the form loads in the user's browser",
            "After the user clicks Save but before server-side validation",
        ],
        "answer": "Before the record is written to the database",
        "explanation": (
            "A 'before' Business Rule fires server-side before the INSERT or UPDATE "
            "hits the DB, letting you modify field values before they are persisted."
        ),
    },
    # ── Application & Module Development ────────────────────────────────────
    {
        "topic": "Application & Module Development",
        "stem": "What is Studio in ServiceNow?",
        "kind": "mcq",
        "options": [
            "An integrated development environment for building scoped applications",
            "A visual report and dashboard builder",
            "A flow diagram tool for documenting processes",
            "A performance benchmarking harness",
        ],
        "answer": "An integrated development environment for building scoped applications",
        "explanation": (
            "Studio provides a single interface to create, edit, and manage all "
            "artifacts (tables, scripts, UI, workflows) belonging to a scoped application."
        ),
    },
    {
        "topic": "Application & Module Development",
        "stem": "What is the key difference between a Global application and a Scoped application in ServiceNow?",
        "kind": "mcq",
        "options": [
            "Scoped apps run in an isolated namespace; Global apps have unrestricted platform access",
            "Global apps come from the Store; Scoped apps are always built in-house",
            "Scoped apps execute faster due to runtime sandbox optimizations",
            "There is no functional difference — the terms are legacy naming conventions",
        ],
        "answer": "Scoped apps run in an isolated namespace; Global apps have unrestricted platform access",
        "explanation": (
            "Scoped apps use a private namespace (e.g., x_acme_) to prevent naming "
            "conflicts and limit cross-app access, improving security and portability."
        ),
    },
    {
        "topic": "Application & Module Development",
        "stem": "What is a Module in the ServiceNow Application Navigator?",
        "kind": "mcq",
        "options": [
            "A navigation link within an application that opens a specific list, form, or URL",
            "A reusable server-side script library",
            "A step inside a Flow Designer flow",
            "A database index definition",
        ],
        "answer": "A navigation link within an application that opens a specific list, form, or URL",
        "explanation": (
            "Modules are the items listed under an application in the navigator. "
            "Each module typically points to a table list, a specific record, or a URL."
        ),
    },
    # ── Reporting ────────────────────────────────────────────────────────────
    {
        "topic": "Reporting",
        "stem": "Which ServiceNow feature tracks KPIs and visualizes trends over time using historical data snapshots?",
        "kind": "mcq",
        "options": [
            "Performance Analytics",
            "Standard Reports",
            "Dashboards",
            "Scheduled Exports",
        ],
        "answer": "Performance Analytics",
        "explanation": (
            "Performance Analytics collects time-series snapshots and lets you chart "
            "trends — unlike standard reports which only reflect current data."
        ),
    },
    {
        "topic": "Reporting",
        "stem": "Where do you navigate to create a new report in ServiceNow?",
        "kind": "mcq",
        "options": [
            "All > Reports > Create New",
            "System Definition > Reports",
            "Performance Analytics > New",
            "System Properties > Reports",
        ],
        "answer": "All > Reports > Create New",
        "explanation": (
            "The Reports module (reachable via All in the navigator) provides the "
            "interface for creating, managing, and scheduling reports."
        ),
    },
    {
        "topic": "Reporting",
        "stem": "Which report type best displays part-to-whole relationships, such as incidents broken down by category?",
        "kind": "mcq",
        "options": ["Pie chart", "Line chart", "Trend chart", "Heatmap"],
        "answer": "Pie chart",
        "explanation": (
            "Pie charts show how individual categories contribute to a whole, "
            "making them ideal for breakdowns like incidents by priority or by category."
        ),
    },
    # ── Service Catalog ──────────────────────────────────────────────────────
    {
        "topic": "Service Catalog",
        "stem": "What is a Catalog Item in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A requestable product or service users can order through the Service Catalog",
            "A configuration record stored in the CMDB",
            "An incident template for common request types",
            "A scheduled maintenance task definition",
        ],
        "answer": "A requestable product or service users can order through the Service Catalog",
        "explanation": (
            "Catalog Items (e.g., 'New Laptop', 'VPN Access') let users request goods "
            "or services, which then trigger fulfillment workflows."
        ),
    },
    {
        "topic": "Service Catalog",
        "stem": "What is a Variable in a Service Catalog item?",
        "kind": "mcq",
        "options": [
            "A form field that collects input from the requester",
            "A JavaScript variable used in catalog client scripts",
            "A price modifier applied based on options selected",
            "A system-generated identifier for each submitted request",
        ],
        "answer": "A form field that collects input from the requester",
        "explanation": (
            "Variables define the questions/fields shown to the user when ordering "
            "a catalog item (e.g., 'Which laptop model do you need?')."
        ),
    },
    {
        "topic": "Service Catalog",
        "stem": "What is the purpose of an Order Guide in the Service Catalog?",
        "kind": "mcq",
        "options": [
            "Groups multiple catalog items into one guided, multi-step request",
            "Provides step-by-step fulfillment instructions for agents",
            "Generates purchase orders for hardware procurement",
            "Defines the approval chain for high-cost catalog requests",
        ],
        "answer": "Groups multiple catalog items into one guided, multi-step request",
        "explanation": (
            "An Order Guide walks a user through selecting from related catalog items "
            "in sequence — ideal for onboarding bundles or multi-item equipment sets."
        ),
    },
    # ── CMDB ─────────────────────────────────────────────────────────────────
    {
        "topic": "CMDB",
        "stem": "What does CMDB stand for?",
        "kind": "mcq",
        "options": [
            "Configuration Management Database",
            "Change Management Data Board",
            "Content Management and Delivery Base",
            "Customer Management Database",
        ],
        "answer": "Configuration Management Database",
        "explanation": (
            "The CMDB is the authoritative repository of Configuration Items (CIs) "
            "and their relationships — the foundation of IT service management."
        ),
    },
    {
        "topic": "CMDB",
        "stem": "What is a Configuration Item (CI) in ServiceNow?",
        "kind": "mcq",
        "options": [
            "Any IT component that must be managed to deliver a service",
            "A customization applied to a ServiceNow form or view",
            "A line item in a service catalog request",
            "An attachment added to a change request",
        ],
        "answer": "Any IT component that must be managed to deliver a service",
        "explanation": (
            "CIs include servers, applications, network devices, and services — "
            "anything tracked in the CMDB to support IT service delivery."
        ),
    },
    {
        "topic": "CMDB",
        "stem": "What is ServiceNow Discovery in the context of the CMDB?",
        "kind": "mcq",
        "options": [
            "An automated process that scans the network to find and populate CI data",
            "A method for end users to report newly purchased IT assets",
            "A global search function for locating any record in the instance",
            "A report that highlights gaps and stale records in the CMDB",
        ],
        "answer": "An automated process that scans the network to find and populate CI data",
        "explanation": (
            "Discovery automatically identifies devices and applications on your network "
            "and populates or updates their CMDB records without manual data entry."
        ),
    },
]
