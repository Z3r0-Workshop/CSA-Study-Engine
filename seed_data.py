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
    # ── User Interface & Navigation (extra) ──────────────────────────────────
    {
        "topic": "User Interface & Navigation",
        "stem": "A user wants to return to the five most recent records they visited without using the Application Navigator. Which UI feature should they use?",
        "kind": "mcq",
        "options": [
            "History tab in the Application Navigator",
            "Breadcrumbs at the top of the content frame",
            "The search bar in the Banner Frame",
            "The Favorites list",
        ],
        "answer": "History tab in the Application Navigator",
        "explanation": (
            "The History tab (clock icon) in the Application Navigator tracks the last "
            "records and lists you visited, letting you jump back without a new search."
        ),
    },
    {
        "topic": "User Interface & Navigation",
        "stem": "On a ServiceNow form, what does a red asterisk (*) next to a field label indicate?",
        "kind": "mcq",
        "options": [
            "The field is mandatory and must be filled before saving",
            "The field value was recently changed",
            "The field is read-only and cannot be edited",
            "The field is only visible to administrators",
        ],
        "answer": "The field is mandatory and must be filled before saving",
        "explanation": (
            "A red asterisk marks a mandatory field. ServiceNow will prevent the record "
            "from saving and display a validation error if the field is left empty."
        ),
    },
    {
        "topic": "User Interface & Navigation",
        "stem": "In one or two sentences, explain the difference between a List view and a Form view in ServiceNow.",
        "kind": "free",
        "options": [],
        "answer": (
            "A List view displays multiple records from a table in rows and columns, "
            "allowing bulk actions and filtering. A Form view displays the full detail "
            "of a single record, showing all its fields for reading or editing."
        ),
        "explanation": (
            "Lists are the entry point for finding records; forms are where you read "
            "or update a specific record. Both are rendered inside the Content Frame."
        ),
    },
    # ── Collaboration (extra) ────────────────────────────────────────────────
    {
        "topic": "Collaboration",
        "stem": "Which area of a record shows a chronological log of all field changes, work notes, and comments in one place?",
        "kind": "mcq",
        "options": [
            "Activity Stream",
            "Audit Log",
            "Work Notes History",
            "Related Lists",
        ],
        "answer": "Activity Stream",
        "explanation": (
            "The Activity Stream (at the bottom of most ITSM forms) combines field "
            "history, work notes, and additional comments in a single timeline view."
        ),
    },
    {
        "topic": "Collaboration",
        "stem": "When an agent writes in the Work Notes field and saves a record, who can see that entry?",
        "kind": "mcq",
        "options": [
            "Only users with the itil role or higher — not the end user (caller)",
            "Everyone who has access to the record, including the caller",
            "Only the assigned agent and their manager",
            "Only administrators with the admin role",
        ],
        "answer": "Only users with the itil role or higher — not the end user (caller)",
        "explanation": (
            "Work Notes are internal. They appear in the Activity Stream for agents "
            "but are hidden from the caller and service portal view."
        ),
    },
    {
        "topic": "Collaboration",
        "stem": "Briefly describe what the Approval feature does in ServiceNow and give one example of where it is commonly used.",
        "kind": "free",
        "options": [],
        "answer": (
            "Approvals pause a workflow or flow and require one or more designated users "
            "to approve or reject before processing continues. A common example is a "
            "Change Request requiring a Change Advisory Board approval before implementation."
        ),
        "explanation": (
            "Approvals are a core governance mechanism in ServiceNow, used in Change "
            "Management, Service Catalog requests, and HR cases to ensure sign-off "
            "before work proceeds."
        ),
    },
    # ── Self-Service & Automation (extra) ────────────────────────────────────
    {
        "topic": "Self-Service & Automation",
        "stem": "What is a Virtual Agent in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A conversational AI chatbot that helps users resolve issues without agent involvement",
            "An automated script that runs on a schedule to process records",
            "A software robot that performs UI actions in the platform",
            "An AI model that predicts incident priority at creation time",
        ],
        "answer": "A conversational AI chatbot that helps users resolve issues without agent involvement",
        "explanation": (
            "Virtual Agent uses NLU-powered conversation flows to guide users to "
            "self-service resolutions — submitting requests, checking ticket status, "
            "or finding knowledge articles — without human agent intervention."
        ),
    },
    {
        "topic": "Self-Service & Automation",
        "stem": "A company wants end users to report a lost laptop through a friendly web interface without accessing the standard ServiceNow backend. What is the most appropriate tool?",
        "kind": "mcq",
        "options": [
            "Service Portal with a Catalog Item",
            "A Business Rule triggered by a table event",
            "A Scheduled Job that polls for email requests",
            "An Import Set that reads from a CSV upload",
        ],
        "answer": "Service Portal with a Catalog Item",
        "explanation": (
            "The Service Portal provides a consumer-style UI where users can browse "
            "catalog items and submit requests. A 'Lost Laptop' catalog item with "
            "variables collects the needed details and triggers fulfillment."
        ),
    },
    {
        "topic": "Self-Service & Automation",
        "stem": "In one or two sentences, explain what Predictive Intelligence does and how it differs from a keyword search.",
        "kind": "free",
        "options": [],
        "answer": (
            "Predictive Intelligence uses machine learning models trained on historical "
            "data to automatically classify, route, or suggest resolutions for records. "
            "Unlike keyword search, it understands context and patterns rather than "
            "matching exact words."
        ),
        "explanation": (
            "Predictive Intelligence is an ML capability — it improves over time as "
            "more data is fed to the model, whereas keyword search is static and "
            "only finds literal matches."
        ),
    },
    # ── Database Management (extra) ──────────────────────────────────────────
    {
        "topic": "Database Management",
        "stem": "Every record in every ServiceNow table has a unique identifier stored in which field?",
        "kind": "mcq",
        "options": [
            "sys_id",
            "record_id",
            "unique_key",
            "table_id",
        ],
        "answer": "sys_id",
        "explanation": (
            "The sys_id is a 32-character GUID automatically assigned to every record "
            "in ServiceNow. It is the primary key used in all cross-table references."
        ),
    },
    {
        "topic": "Database Management",
        "stem": "What is a Reference field in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A field that points to a record in another table and displays its display value",
            "A read-only field that mirrors the value of another field on the same form",
            "A field that stores a URL or hyperlink",
            "A field calculated by a formula at display time",
        ],
        "answer": "A field that points to a record in another table and displays its display value",
        "explanation": (
            "A Reference field stores the sys_id of the target record but displays "
            "that record's display value (e.g., a user's full name). The underlying "
            "database value is always the sys_id."
        ),
    },
    {
        "topic": "Database Management",
        "stem": "What is an Import Set in ServiceNow and what problem does it solve?",
        "kind": "free",
        "options": [],
        "answer": (
            "An Import Set is a staging table that receives raw data from an external "
            "source such as a CSV or web service. A Transform Map then maps and "
            "coalesces that data into the target ServiceNow table, solving the problem "
            "of safely loading external data without corrupting existing records."
        ),
        "explanation": (
            "The two-step import (load into staging, then transform) lets you preview "
            "and validate data before it touches production tables, and the coalesce "
            "key prevents duplicate record creation."
        ),
    },
    # ── Workflow & Automation (extra) ────────────────────────────────────────
    {
        "topic": "Workflow & Automation",
        "stem": "A Script Include in ServiceNow is best described as:",
        "kind": "mcq",
        "options": [
            "A reusable server-side JavaScript class or function library callable from other scripts",
            "A client-side script that runs when a form field changes",
            "A scheduled server-side script that runs at a defined interval",
            "A REST API endpoint definition",
        ],
        "answer": "A reusable server-side JavaScript class or function library callable from other scripts",
        "explanation": (
            "Script Includes are server-side libraries. You define a class once and "
            "call it from Business Rules, Flow Designer scripts, or REST endpoints, "
            "keeping logic in one maintainable place."
        ),
    },
    {
        "topic": "Workflow & Automation",
        "stem": "You need to send a customised email whenever an Incident priority changes to Critical. What is the recommended decoupled approach?",
        "kind": "mcq",
        "options": [
            "Fire a platform Event from a Business Rule; create a Notification that triggers on that Event",
            "Call gs.sendEmail() directly inside a Business Rule",
            "Use a Scheduled Job to poll for Critical incidents every minute",
            "Create a UI Action button that agents click to manually send the email",
        ],
        "answer": "Fire a platform Event from a Business Rule; create a Notification that triggers on that Event",
        "explanation": (
            "Events decouple the trigger (Business Rule) from the messaging (Notification). "
            "This means the email logic can change independently of the detection logic, "
            "and multiple notifications can subscribe to the same event."
        ),
    },
    {
        "topic": "Workflow & Automation",
        "stem": "In one or two sentences, explain the difference between a 'before' and an 'after' Business Rule.",
        "kind": "free",
        "options": [],
        "answer": (
            "A 'before' Business Rule runs server-side before the record is written to "
            "the database, allowing you to modify field values before they are persisted. "
            "An 'after' Business Rule runs after the database write has committed, "
            "so the record already has its final saved values."
        ),
        "explanation": (
            "Use 'before' when you need to change what gets saved. Use 'after' when "
            "you need to react to what was saved — for example, creating a related "
            "record or sending a notification based on the committed values."
        ),
    },
    # ── Application & Module Development (extra) ─────────────────────────────
    {
        "topic": "Application & Module Development",
        "stem": "What is an Update Set in ServiceNow?",
        "kind": "mcq",
        "options": [
            "A container that captures configuration changes so they can be moved between instances",
            "A batch of database records exported for backup purposes",
            "A script that automatically upgrades the platform to a new version",
            "A set of field-level defaults applied when a new record is created",
        ],
        "answer": "A container that captures configuration changes so they can be moved between instances",
        "explanation": (
            "Update Sets record every configuration change made while they are active. "
            "You retrieve and commit them on a target instance (e.g., Production) to "
            "promote changes from Development or Test."
        ),
    },
    {
        "topic": "Application & Module Development",
        "stem": "Which role does a user need to create and manage Update Sets in a non-production ServiceNow instance?",
        "kind": "mcq",
        "options": [
            "admin",
            "itil",
            "catalog_admin",
            "report_admin",
        ],
        "answer": "admin",
        "explanation": (
            "Managing Update Sets — creating, switching, exporting, and committing — "
            "requires the admin role. The itil role is for ITSM process work, not "
            "platform configuration management."
        ),
    },
    {
        "topic": "Application & Module Development",
        "stem": "What problem does application scoping solve, and how does the namespace prefix (e.g., x_acme_) help?",
        "kind": "free",
        "options": [],
        "answer": (
            "Application scoping isolates a custom application's artifacts from global "
            "and other scoped applications, preventing naming conflicts and accidental "
            "cross-app interference. The namespace prefix (e.g., x_acme_) ensures that "
            "tables, script includes, and other artifacts have unique names across "
            "the entire instance."
        ),
        "explanation": (
            "Without scoping, two apps could define a table or script with the same "
            "name and overwrite each other. Scoping is also required for apps published "
            "to the ServiceNow Store."
        ),
    },
    # ── Reporting (extra) ────────────────────────────────────────────────────
    {
        "topic": "Reporting",
        "stem": "Which report type is best for showing how a value — such as the number of open incidents — has changed week over week?",
        "kind": "mcq",
        "options": [
            "Trend (line) chart",
            "Pie chart",
            "Single Score",
            "Heatmap",
        ],
        "answer": "Trend (line) chart",
        "explanation": (
            "A Trend chart plots values over time intervals (daily, weekly, monthly), "
            "making it the right choice for visualising movement — increases, decreases, "
            "or plateaus — in a metric over a period."
        ),
    },
    {
        "topic": "Reporting",
        "stem": "How can you share a ServiceNow report with a user who does not have a ServiceNow login?",
        "kind": "mcq",
        "options": [
            "Schedule the report to be emailed as a PDF or CSV attachment",
            "Grant them a temporary guest session token",
            "Export the report to a shared network drive via FTP",
            "Reports cannot be shared outside the platform",
        ],
        "answer": "Schedule the report to be emailed as a PDF or CSV attachment",
        "explanation": (
            "Scheduled reports can be sent to any email address as a PDF, Excel, or "
            "CSV attachment on a recurring basis — no ServiceNow account required "
            "by the recipient."
        ),
    },
    {
        "topic": "Reporting",
        "stem": "In one or two sentences, explain the difference between a standard Report and Performance Analytics in ServiceNow.",
        "kind": "free",
        "options": [],
        "answer": (
            "A standard Report runs against live data and shows the current state of "
            "records at the time it is run. Performance Analytics collects scheduled "
            "data snapshots over time and lets you track trends and KPIs historically."
        ),
        "explanation": (
            "Standard reports answer 'what is true right now?' Performance Analytics "
            "answers 'how has this changed over time?' — it requires the PA plugin "
            "and scheduled data collection jobs to be configured."
        ),
    },
    # ── Service Catalog (extra) ──────────────────────────────────────────────
    {
        "topic": "Service Catalog",
        "stem": "What is a Record Producer in the Service Catalog?",
        "kind": "mcq",
        "options": [
            "A catalog item that creates a record in any table (not just sc_request) when submitted",
            "A scheduled job that auto-creates catalog request records",
            "A script that generates catalog items from a template",
            "A report that lists all submitted service requests",
        ],
        "answer": "A catalog item that creates a record in any table (not just sc_request) when submitted",
        "explanation": (
            "A Record Producer lets users submit a form through the Service Portal "
            "that creates a record directly in a specified table — for example, an "
            "Incident or HR Case — giving a consumer-friendly front end to any process."
        ),
    },
    {
        "topic": "Service Catalog",
        "stem": "A Catalog UI Policy differs from a regular UI Policy because:",
        "kind": "mcq",
        "options": [
            "It runs on Service Catalog variable fields rather than standard table fields",
            "It executes server-side instead of client-side",
            "It applies to every form across all tables simultaneously",
            "It can only hide or show fields, not make them mandatory",
        ],
        "answer": "It runs on Service Catalog variable fields rather than standard table fields",
        "explanation": (
            "Catalog UI Policies control the behaviour (mandatory, read-only, visible) "
            "of catalog item variables. Standard UI Policies operate on regular table "
            "fields and do not reach catalog variables."
        ),
    },
    {
        "topic": "Service Catalog",
        "stem": "Briefly explain what a Catalog Client Script is and give one example of when you would use it.",
        "kind": "free",
        "options": [],
        "answer": (
            "A Catalog Client Script is a client-side JavaScript that runs on a "
            "catalog item form in response to events like onLoad, onChange, or "
            "onSubmit. For example, you could use an onChange script to show or hide "
            "additional variable questions based on the option a user selects."
        ),
        "explanation": (
            "They are the catalog equivalent of regular Client Scripts. They operate "
            "on catalog variables rather than standard form fields and only run "
            "in the browser — not on the server."
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
    # ── CMDB (extra) ─────────────────────────────────────────────────────────
    {
        "topic": "CMDB",
        "stem": "Which CMDB table is the parent class for all Configuration Item types in ServiceNow?",
        "kind": "mcq",
        "options": [
            "cmdb_ci",
            "cmdb",
            "task",
            "asset",
        ],
        "answer": "cmdb_ci",
        "explanation": (
            "All CI classes (servers, applications, network gear, etc.) extend cmdb_ci. "
            "This inheritance means every CI carries the base fields defined on that "
            "parent table, such as name, managed by, and support group."
        ),
    },
    {
        "topic": "CMDB",
        "stem": "What is a CI Relationship in the ServiceNow CMDB?",
        "kind": "mcq",
        "options": [
            "A typed link between two CIs that describes how they depend on or connect to each other",
            "An approval chain that governs which teams can modify a CI record",
            "A scheduled scan that checks if a CI is still reachable on the network",
            "A report that shows all changes made to a single CI over time",
        ],
        "answer": "A typed link between two CIs that describes how they depend on or connect to each other",
        "explanation": (
            "CI Relationships (e.g., 'Runs on', 'Depends on', 'Hosted on') connect "
            "CIs into a dependency map. This is critical for impact analysis — knowing "
            "which services are affected when a server goes down."
        ),
    },
    {
        "topic": "CMDB",
        "stem": "In one or two sentences, explain why keeping the CMDB accurate matters for Incident Management.",
        "kind": "free",
        "options": [],
        "answer": (
            "An accurate CMDB lets agents quickly identify which CIs are affected by "
            "an incident and trace upstream or downstream dependencies, reducing "
            "mean time to resolution. It also enables automatic population of the "
            "'Configuration item' field, linking the incident to the correct asset "
            "for reporting and SLA tracking."
        ),
        "explanation": (
            "When CMDB data is stale or missing, agents waste time identifying "
            "affected systems manually, impact assessment is guesswork, and post-incident "
            "reports lack the CI context needed for root cause analysis."
        ),
    },
]
