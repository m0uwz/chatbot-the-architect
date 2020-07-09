import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, backref
import sqlalchemy.dialects.postgresql as sql

# TOCHANGE
#eng = create_engine("postgresql+psycopg2://postgres:admin@/chatbot")
eng = create_engine("postgresql+psycopg2://admin:admin@chatbot-db/")


Base = declarative_base()

class LectureHasCourseItem(Base):
    __tablename__ = 'lecture_has_course_item'
    lecture_id = Column(Integer, ForeignKey('lecture.id'), primary_key=True)
    course_item_id = Column(Integer, ForeignKey('course_item.id'), primary_key=True)

class SubtaskHasCourseItem(Base):
    __tablename__ = 'subtask_has_course_item'
    subtask_id = Column('subtask_id', Integer, ForeignKey('subtask.id'), primary_key=True)
    course_item_id = Column('course_item_id', Integer, ForeignKey('course_item.id'), primary_key=True)
    how_to_exercise_specific = Column(String)
    course_item = relationship("CourseItem", back_populates="relationship_subtasks")
    subtask = relationship("Subtask", back_populates="relationship_course_items")

class CourseItem(Base):
    __tablename__ = "course_item"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    how_to = Column(String)
    link = Column(String)
    file = Column(String)
    relationship_subtasks = relationship("SubtaskHasCourseItem", back_populates="course_item")                    

class Lecture(Base):
    __tablename__ = "lecture"
    id = Column(Integer, primary_key=True)
    chapter = Column(Integer)
    title = Column(String)
    file = Column(String)          
    course_items = relationship(
        "CourseItem",
        secondary='lecture_has_course_item',
        primaryjoin="Lecture.id == LectureHasCourseItem.lecture_id",
        backref="lectures")

class Exercise(Base):
    __tablename__ = "exercise"
    id = Column(Integer, primary_key=True)
    exercise_no = Column(Integer)
    title = Column(String)

class Subtask(Base):
    __tablename__ = "subtask"
    id = Column(Integer, primary_key=True)
    subtask_no = Column(Integer)
    exercise_id = Column(Integer, ForeignKey('exercise.id', ondelete='CASCADE'))
    exercise = relationship(
        "Exercise",
        backref=backref("subtasks",
                        uselist=True,
                        cascade='delete,all'))
    relationship_course_items = relationship("SubtaskHasCourseItem", back_populates="subtask")
    

Base.metadata.bind = eng      
Base.metadata.drop_all()
Base.metadata.create_all()        
        
DBSession = sessionmaker(bind=eng)
session = DBSession()   

# Add course items
list_course_items_chapter_2 = [
        CourseItem(
            id = 1,
            title = 'System design',
            description = 'System design is the process of defining the architecture, modules, interfaces, and data for a system to satisfy specified requirements.',
            how_to = None,
            link = 'https://en.wikipedia.org/wiki/Systems_design',
            file = None),
        CourseItem(
            id = 2,
            title = 'Unit testing',
            description = 'In computer programming, unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine whether they are fit for use.',
            how_to = None,
            link = 'https://en.wikipedia.org/wiki/Unit_testing',
            file = 'https://martinfowler.com/bliki/images/unitTest/sketch.png'), 
        CourseItem(
            id = 3,
            title = 'Integration architecture',
            description = 'There are multiple definitions for Integration architecture but here is one by Professor Alda: An integration architecture defines **global design decisions** for the integration of potentially *distributed* and *heterogeneous* software components. An integration architecture also makes **implications for tools and frameworks** for developing, testing, andmaintaining *interoperable* software.',
            how_to = None,
            link = None,
            file = None), 
        CourseItem(
            id = 4,
            title = 'Architectural styles',
            description = 'Software architecture styles define rules and assumptions for a type (template, class) of software architectures. That means, that the concrete  implementation of a software architecture of a software is an instance of a software architecture style. Here I have an example of the Layer pattern for you:',
            how_to = None,
            link = None,
            file = None), # 'http://www.ruanyifeng.com/blogimg/asset/2016/bg2016090302.png'
        CourseItem(
            id = 5,
            title = 'Architectural patterns',
            description = 'Software architecture styles define rules and assumptions for a type (template, class) of software architectures. That means, that the concrete  implementation of a software architecture of a software is an instance of a software architecture style. Here I have an example of the Layer pattern for you:',
            how_to = None,
            link = None,
            file = None), # 'http://www.ruanyifeng.com/blogimg/asset/2016/bg2016090302.png'),
        CourseItem(
            id = 6,
            title = 'Software Architecture',
            description = 'A software architecture describes the decomposition of a software system that follows the specifications of pertaining architectural styles. The description of a software architecture comprises the following constituting elements: The fundamental **architecture elements** and their **interfaces**, the **interaction relationships** among those architecture elements as well as the **architecture directives**, and the characteristic **factors describing the economic value** of the whole software architecture.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 7,
            title = 'Architecture elements',
            description = 'The architecture elements describe atomic units (e.g. classes, modules) and complex units (e.g. subsystems, packages) of a software architecture.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 8,
            title = 'Interaction relationships',
            description = 'Architecture elements have to interact with each other. The easiest way is probably the local interaction via a local method call. But there are also more advanced models like the Observer Pattern.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 9,
            title = 'Non-blocking asynchronous interaction',
            description = 'Non-blocking or asynchronous interaction: The sender is not blocked, may receive or initiate further requests; stays responsive. Notification e.g., by a callback function.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 10,
            title = 'Blocking synchronous interaction',
            description = 'Blocking or synchronous interaction: The sender remains blocked, has to await the answer (response).',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 11,
            title = 'Conway\'s law',
            description = 'Conway\'s Law says: \'Organizations which design systems [...] are constrained to produce designs which are copies of the communication structures of these organizations.\' Let\'s interpret that: The software architecture of a system is influenced by formal and informal organizational structures.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 12,
            title = 'Architecture directives',
            description = 'Architecture Directives are additional properties, rules, and restrictions on a software architecture that cannot be directly inferred by the decomposition of the software, for instance quality control or design of security aspects.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 13,
            title = 'Economic value',
            description = 'Characteristic factors for describing the economic value are usually identified on a business level, but are evaluated on an architectural level at runtime. Examples: SLA (contractual agreement between client und provider) and KPI (functional measurements that can be extracted during runtime).',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 14,
            title = 'SLA',
            description = 'Characteristic factors for describing the economic value are usually identified on a business level, but are evaluated on an architectural level at runtime. Examples: SLA (contractual agreement between client und provider) and KPI (functional measurements that can be extracted during runtime).',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 15,
            title = 'KPI',
            description = 'Characteristic factors for describing the economic value are usually identified on a business level, but are evaluated on an architectural level at runtime. Examples: SLA (contractual agreement between client und provider) and KPI (functional measurements that can be extracted during runtime).',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 16,
            title = 'Legacy system',
            description = 'A legacy system is an old computer system or application program, which is still in use. Often referencing a system as legacy means that it paved the way for the standards that would follow it. This can also imply that the system is out of date or in need of replacement.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 17,
            title = 'API',
            description = 'An application programming interface (API) is a computing interface which defines interactions between multiple software intermediaries. It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used, the conventions to follow, etc.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 18,
            title = 'Monolithic architecture',
            description = 'There is no separation of application logic, data storage, and user interface (e.g., Mainframe-Batch programs).',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 19,
            title = 'Data transfer',
            description = 'Data transfer is a basic concept of integration: An application writes into a file, while another application reads from the same after a while.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 20,
            title = 'Shared database',
            description = 'The shared database is a basic concept of integration: Various systems use a global databasefor sharing data.',
            how_to = None,
            link = None,
            file = 'http://diarchitect-chatbot.de:8080/course_items/shared-file.png'),
        CourseItem(
            id = 21,
            title = 'Methods calls',
            description = 'Method calls are a basic concept of integration: A system provides an API that can be accessed by Remote Procedure Calls (RPC) in a synchronous way.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 22,
            title = 'Messaging',
            description = 'Messaging is a basic concept of integration: A system sends messages to common message channel in an asynchronousway. Receiver component can read the message later on.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 23,
            title = 'Point-to-Point',
            description = 'Point-to-Point is a basic integration pattern: There is a direct connection of the corresponding interfaces.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 24,
            title = 'Hub and Spoke',
            description = 'Hub and Spoke is a basic integration pattern: All systems were integrated from a single location, the hub. The state is maintained in a shared database and there is only a single point of integration and transformation.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 25,
            title = 'Bus',
            description = 'A Bus is a basic integration pattern: Adapters are used for transformation. There is no state maintained and add-on services such as routing required.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 26,
            title = '4 Views Model',
            description = 'The 4 Views Model includes the modelling of the environment of the system under development, indicating the most relevant dependencies. It consists of four views: **Context view**, **runtime view**, **module view** and **distribution view**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 27,
            title = 'Module view',
            description = 'The Module View is part of the **4 Views Model** and it models static structures of the architecture elements of the system, subsystems, components, classes and their interfaces. It represents the dependencies among these elements. For representation, **UML Component Diagrams**, **UML Package Diagrams** and **UML Class Diagrams** were used.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 28,
            title = 'Runtime View',
            description = 'The Runtime View is part of the **4 Views Model** and describes, which architecture elements (classes, objects, subsystems, components,...) of a systems do exist at runtime and how they interact together (dynamic perspective). Actors can also be included, too. For representation, **UML Sequence Diagrams** were used.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 29,
            title = 'Context View',
            description = 'The Context View is part of the **4 Views Model** and models the environment of the system under development, indicating the most relevant dependencies. It is the abstract modelling of the system as a black box to the neighboring system (no internal structure is to be revealed). For representation, **UML Package Diagrams** were used.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 30,
            title = 'Distribution View',
            description = 'The Distribution View is part of the **4 Views Model** and it describes the runtime environments of the system in terms of hardware devices (e.g., server network, firewalls) and the corresponding protocolls. It also represents the  execution environments (e.g., application server, container). For representation, **UML Distribution Diagrams** were used.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 31,
            title = 'UML Component Diagram',
            description = 'An UML Component Diagram represents the architecture elements (subsystems, components) of a system as organized during runtime. The interfaces were modelled explicitly (required and provided) and the components were modelled as white boxes with dedicated connections from internal implementations to external interfaces. The UML Component Diagram is used for the **Module View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 32,
            title = 'UML Package Diagram',
            description = 'Package Diagrams show an overview of the decomposition of the complete system in packages and subsystems. They were used for the **Context View** and the **Module View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 33,
            title = 'UML Distribution Diagram',
            description = 'An UML Distribution Diagram represents the hardware topology as well as the distribution of the software to the hardware. It is used for the **Distribution View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 34,
            title = 'UML Sequence Diagram',
            description = 'A sequence diagram shows object interactions arranged in time sequence. It depicts the objects and classes involved in the scenario and the sequence of messages exchanged between the objects needed to carry out the functionality of the scenario. It is used for the **Runtime View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 35,
            title = 'UML Class Diagram',
            description = 'A Class Diagram is a type of static structure diagram that describes the structure of a system by showing the system\'s classes, their attributes, operations (or methods), and the relationships among objects. It is used for the **Module View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 36,
            title = 'Layer Pattern',
            description = 'The Layer Pattern is the decomposition of system functionality in single layers: Presentation Layer, Application Layer, Domain Layer and Infrastructure Layer.  Each layer implements a coherent functionality block on a given abstraction level and provides services for the lower layers (or same level). Each layer can be developed, deployed, and maintained independently.',
            how_to = None,
            link = None,
            file = None)
    ]
list_course_items_chapter_3 = [
        CourseItem(
            id = 37,
            title = 'API',
            description = 'An **API** specifies the operations as well as the input and output data of a software component. The core idea is to have a set of functions independent of their implementation. If the implementation changes, then this will have no effect on the consumers of the software components. There are different types of APIs: **Object-oriented API**, **REST-based API** and **Messaging-API**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 38,
            title = 'Object-oriented API',
            description = 'An **object-oriented API** is a language-based API, so it is language dependent. Example: Java-API of a framework like JDBC. You will have local access only. There are also two different types of APIs that both have remote access: **REST-based API** and **Messaging-API**',
            how_to = None,
            link = 'https://en.wikipedia.org/wiki/Unit_testing',
            file = 'https://martinfowler.com/bliki/images/unitTest/sketch.png'), 
        CourseItem(
            id = 39,
            title = 'REST-based API',
            description = '**REST-based API**: REST stands for REpresentational State Transfer, API for Application Programming Interface. This means a programming interface that is based on the paradigms and behavior of the World Wide Web (WWW) and describes an approach for communication between client and server in networks via the HTTP protocol.',
            how_to = None,
            link = None,
            file = "http://diarchitect-chatbot.de:8080/course_items/rest-based-api.png"),
        CourseItem(
            id = 40,
            title = 'Messaging-API',
            description = '**Messaging-APIs** are langugage and platform independet. You will have a strong decoupling of provider and consumer because the provider can send push messages to the consumer, even if the consumer is offline.',
            how_to = None,
            link = None,
            file = None), 
        CourseItem(
            id = 41,
            title = 'CRUD',
            description = '**Create, Read, Update, and Delete (CRUD)** are the four basic functions to maintain your entities. It is recommended that an API provide these methods for controlling your entity objects.',
            how_to = None,
            link = None,
            file = None), 
        CourseItem(
            id = 42,
            title = 'HTTP methods',
            description = '**HTTP** defines a set of **request methods** to indicate the desired action to be performed for a given resource. The most important methods are **GET**, **POST**, **PUT** and **DELETE**. These HTTP methods were used to communicate with a **REST-based API**.',
            how_to = None,
            link = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods",
            file = "http://diarchitect-chatbot.de:8080/course_items/rest-based-api.png"),
        CourseItem(
            id = 43,
            title = 'JSON',
            description = '**JSON** is is a lightweight data-interchange format that can be parsed and consumed easily by modern programming languages. It consists of name/value pairs and arrays.',
            how_to = None,
            link = "https://www.w3schools.com/js/js_json_intro.asp",
            file = "https://www.datapopulator.com/data.png"),
        CourseItem(
            id = 44,
            title = 'HTTP',
            description = '**HTTP** is a protocol which allows the fetching of resources (e.g., HTML documents). It is the foundation of any data exchange on the Web and it is a client-server protocol, which means requests are initiated by the recipient, usually the Web browser. Ask me about **HTTP methods** and I can tell you further details.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 45,
            title = 'URI',
            description = 'An **URI** (Uniform Resource Identifier) is a string that refers to a resource. The most common are **URLs**, which identify the resource by giving its location on the Web. In **REST**, resources can be arranged in a hierarchical order. Given the hierarchical order, they can be identified and, thus, accessed by an **URI**.',
            how_to = None,
            link = None,
            file = "https://i.stack.imgur.com/2iD7U.jpg"),
        CourseItem(
            id = 46,
            title = 'URL',
            description = '**Uniform Resource Locator (URL)** is a text string that specifies where a resource (such as a web page, image, or video) can be found on the Internet. In the context of **HTTP**, URLs are called "Web address" or "link".',
            how_to = None,
            link = "https://developer.mozilla.org/en-US/docs/Glossary/URL",
            file = "https://i.stack.imgur.com/2iD7U.jpg"),
        CourseItem(
            id = 47,
            title = 'Spring Boot',
            description = '**Spring Boot** is an open source Java-based framework used to create a microservice. Spring Boot offers both a mature development model and an execution environment for **REST-based APIs**. ',
            how_to = None,
            link = "https://spring.io/projects/spring-boot",
            file = None),
        CourseItem(
            id = 48,
            title = 'Microservice',
            description = '**Microservice** is an architecture that allows the developers to develop and deploy services independently. Each service running has its own process and this achieves the lightweight model to support business applications.',
            how_to = None,
            link = "https://www.tutorialspoint.com/spring_boot/spring_boot_introduction.htm",
            file = "https://static1.smartbear.co/smartbearbrand/files/f3/f348bd41-8bd6-4f6d-b156-f178a90452af.png"),
        CourseItem(
            id = 49,
            title = 'Swagger',
            description = '**Swagger** is a collection of tools for both the documentation and the development of **REST-based APIs**, pertaining server skeletons as well as client proxies.',
            how_to = None,
            link = "https://swagger.io/tools/open-source/getting-started",
            file = "https://i1.wp.com/springframework.guru/wp-content/uploads/2017/02/swagger-ui_with_default_endpoint_documentation.png?resize=863%2C593&ssl=1"),
        CourseItem(
            id = 50,
            title = 'Postman',
            description = 'Postman is a powerful tool for developing and testing APIs. You can save a collection of HTTP requests and send them to an API. You get the result within the tool.',
            how_to = None,
            link = "https://learning.postman.com/getting-started/",
            file = "https://www.socketlabs.com/wp-content/uploads/2019/04/postman.png")
    ]
list_course_items_chapter_4 = [    
        CourseItem(
            id = 51,
            title = 'Node.js',
            description = '**Node.js** is an application framework for developing network-based applications. It is based on a module concept which can be flexibly integrated by the **NPM Package Manager**. The basic language for writing Node.js applications is **JavaScript**. It is basically a **runtime environment** that executes JavaScript code outside a web browser. If you want to use it, you can follow the tutorial here:',
            how_to = None,
            link = 'https://www.w3schools.com/nodejs/nodejs_get_started.asp',
            file = None),
        CourseItem(
            id = 52,
            title = 'JavaScript',
            description = 'JavaScript is a scripting language that was originally developed for dynamic HTML in web browsers in order to evaluate user interactions, change, reload or generate content and thus expand the possibilities of HTML and CSS. Today JavaScript is also used outside of browsers, for example with **Node.js** on servers.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 53,
            title = 'Runtime environment',
            description = 'A **runtime environment** describes the requirements of a certain runtime system that are available and defined during the runtime of computer programs. This is defined by the elementary components of the programming language such as the behavior of language constructs and other functions such as type testing, debugging, code generation and optimization. For example, **Node.js** is a runtime environment for **JavaScript**.',
            how_to = None,
            link = 'https://www.techopedia.com/definition/5466/runtime-environment-rte',
            file = None),
        CourseItem(
            id = 54,
            title = 'npm Package Manager',
            description = '**npm** is a package manager for the **JavaScript** runtime environment **Node.js**. The most important architecture element is the NPM Registry, in which packages can be published from a provider. The NPM Registry can be accessed by a **CLI** (Command Line Interface).',
            how_to = None,
            link = 'https://www.npmjs.com/',
            file = None),
        CourseItem(
            id = 55,
            title = 'NPM',
            description = '**npm** is a package manager for the **JavaScript** runtime environment **Node.js**. The most important architecture element is the NPM Registry, in which packages can be published from a provider. The NPM Registry can be accessed by a **CLI** (Command Line Interface).',
            how_to = None,
            link = 'https://www.npmjs.com/',
            file = None),
        CourseItem(
            id = 56,
            title = 'CLI',
            description = 'A **command-line interface (CLI)** processes commands to a computer program in the form of lines of text.',
            how_to = None,
            link = 'https://www.w3schools.com/whatis/whatis_cli.asp',
            file = 'https://i.stack.imgur.com/DRJPd.jpg'),
        CourseItem(
            id = 57,
            title = 'Express.js',
            description = '**Express.js** is a package written for Node.js providing a Web framework that allows to implement modern web applications as **REST-based APIs**. You can define routes for **routing** explicitly for managing resources according to the **CRUD** paradigm. **HTTP methods** are given by the **API**.',
            how_to = None,
            link = None,
            file = 'https://devopedia.org/images/article/157/9305.1551338805.png'),
        CourseItem(
            id = 58,
            title = 'Routing',
            description = '**Routing** refers to how an application’s endpoints (**URIs**) respond to client requests (**HTTP**).',
            how_to = None,
            link = 'https://expressjs.com/en/guide/routing.html',
            file = 'https://i0.wp.com/technotip.com/wp-content/uploads/nodejs/routes-node-server-request-response-technotip.png?resize=538%2C294&ssl=1'),
        CourseItem(
            id = 59,
            title = 'MongoDB',
            description = '**MongoDB** is a document-oriented NoSQL database. Since the database is document-oriented, it can manage collections of **JSON**-like documents. The MongoDB is part of the **MEAN-Stack**.',
            how_to = None,
            link = 'https://www.mongodb.com/',
            file = None),
        CourseItem(
            id = 60,
            title = 'MEAN Stack',
            description = 'The **MEAN Stack** is a free and open-source JavaScript software stack for building dynamic web sites and web applications. It consists of **MongoDB**, **Express.js**, **Angular** and **Node.js**.',
            how_to = None,
            link = None,
            file = 'https://www.anblicks.com/wp-content/uploads/2018/09/MEANSTACK-concept.png')
]
list_course_items_chapter_5 = [
        CourseItem(
            id = 61,
            title = 'Shared file',
            description = 'You can integrate software based on data via a **shared file**: An application writes into a file, while another application reads from the same after a while. Here it is necessary that there is an agreement on a common path to the file.',
            how_to = None,
            link = None,
            file = 'http://diarchitect-chatbot.de:8080/course_items/shared-file.png'),
        CourseItem(
            id = 62,
            title = 'Remote procedure call',
            description = 'The integration based on calling provided functions within a different process environment is called **Remote Procedure Call (RPC)**.',
            how_to = None,
            link = None,
            file = 'http://diarchitect-chatbot.de:8080/course_items/remote-procedure-call.png'),
        CourseItem(
            id = 63,
            title = 'Integration styles',
            description = 'There are different styles to integrate distributed software components: **Shared file**, **shared database**, **remote procedure call** and **messaging**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 64,
            title = 'SOAP',
            description = 'SOAP is a XML-based message format used for the interaction with a Web Service.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 65,
            title = 'MOM',
            description = 'A dedicated communication subsystem called **message-oriented middleware (MOM)** conveys data along channels (or queues). Channels store messages until they are consumed (read) by a receiving subsystem. This supports the integration style **messaging**.',
            how_to = None,
            link = None,
            file = 'http://diarchitect-chatbot.de:8080/course_items/mom.png'),
        CourseItem(
            id = 66,
            title = 'Message-oriented Middleware',
            description = 'A dedicated communication subsystem called **message-oriented middleware (MOM)** conveys data along channels (or queues). Channels store messages until they are consumed (read) by a receiving subsystem. This supports the integration style **messaging**.',
            how_to = None,
            link = None,
            file = 'http://diarchitect-chatbot.de:8080/course_items/mom.png'),
        CourseItem(
            id = 67,
            title = 'Message patterns',
            description = 'There are some patterns for **Message-based Middleware (MOM)** systems: **Request Reply Pattern**, **Return Address Pattern**, **Multiple Service Providers Pattern**, **Multiple Service Providers with Correlation IDs Pattern**, **Routing Message Router Pattern**, **Message Translator Pattern**, **Content Enricher Pattern**, **Content Filter Pattern**, **Splitter Pattern** and **Aggregator Pattern**.',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 68,
            title = 'Request Reply Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 69,
            title = 'Return Address Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 70,
            title = 'Multiple Service Providers Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 71,
            title = 'Multiple Service Providers with Correlation IDs Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 72,
            title = 'Routing Message Router Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 73,
            title = 'Message Translator Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 74,
            title = 'Content Enricher Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 75,
            title = 'Content Filter Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 76,
            title = 'Splitter Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None),
        CourseItem(
            id = 77,
            title = 'Aggregator Pattern',
            description = 'TODO',
            how_to = None,
            link = None,
            file = None)
    ]

session.add_all(list_course_items_chapter_2)
session.add_all(list_course_items_chapter_3)
session.add_all(list_course_items_chapter_4)
session.add_all(list_course_items_chapter_5)


# Add lectures
session.add_all(
    [
        Lecture(
            id = 1,
            chapter = 1,
            title = 'Introduction and Organization, First View on Integration Architecture',
            file =  None),
        Lecture(
            id = 2,
            chapter = 2,
            title = 'Introduction to Software Architectures and Architectural Integration',
            file = None), 
        Lecture(
            id = 3,
            chapter = 2,
            title = 'Introduction to Software Architectures and Architectural Integration',
            file = None), 
        Lecture(
            id = 4,
            chapter = 2,
            title = 'Introduction to Software Architectures and Architectural Integration',
            file = None), 
        Lecture(
            id = 5,
            chapter = 3,
            title = 'A deeper look on Architectural Integration: Solutions and Patterns',
            file = None), 
        Lecture(
            id = 6,
            chapter = 4,
            title = 'Patterns and Tools for Interface Integration Testing',
            file = None), 
        Lecture(
            id = 7,
            chapter = 5,
            title = 'Message-Oriented Middleware (MOM) -StateOf-The-Art solutions',
            file = None) 
    ]
)

# Add exercises
session.add_all(
    [
        Exercise(
            id = 1,
            exercise_no = 1,
            title = 'Public API'), 
        Exercise(
            id = 2,
            exercise_no = 2,
            title = 'Migration of application to REST'), 
        Exercise(
            id = 3,
            exercise_no = 3,
            title = 'Migration of application to Node.js'), 
        Exercise(
            id = 4,
            exercise_no = 4,
            title = 'Integration Testing'), 
        Exercise(
            id = 5,
            exercise_no = 5,
            title = 'UI Integration'), 
        Exercise(
            id = 6,
            exercise_no = 6,
            title = 'Semesterproject')
    ]
)

# Add subtasks
session.add_all(
    [
        Subtask(
            id = 1,
            subtask_no = 1,
            exercise_id = 1),
        Subtask(
            id = 2,
            subtask_no = 2,
            exercise_id = 1),
        Subtask(
            id = 3,
            subtask_no = 1,
            exercise_id = 2),
        Subtask(
            id = 4,
            subtask_no = 2,
            exercise_id = 2),
        Subtask(
            id = 5,
            subtask_no = 1,
            exercise_id = 3),
        Subtask(
            id = 6,
            subtask_no = 2,
            exercise_id = 3),
        Subtask(
            id = 7,
            subtask_no = 3,
            exercise_id = 3),    
        Subtask(
            id = 8,
            subtask_no = 4,
            exercise_id = 3),
        Subtask(
            id = 9,
            subtask_no = 1,
            exercise_id = 4),
        Subtask(
            id = 10,
            subtask_no = 2,
            exercise_id = 4),
        Subtask(
            id = 11,
            subtask_no = 3,
            exercise_id = 4),
        Subtask(
            id = 12,
            subtask_no = 1,
            exercise_id = 5),
        Subtask(
            id = 13,
            subtask_no = 1,
            exercise_id = 6) 
    ]
)

session.commit()

# Add lecture has course item
session.add_all(
    [
        LectureHasCourseItem(
            lecture_id = 1,
            course_item_id = 1),
        LectureHasCourseItem(
            lecture_id = 1,
            course_item_id = 2
        )
    ]
)

# Add subtask has course item
session.add_all(
    [
        SubtaskHasCourseItem(
            subtask_id = 1,
            course_item_id = 32,
            how_to_exercise_specific = "Model the context view with an UML Package Diagram. One component could be the OrangeHRM enterprise software, for example."),
        SubtaskHasCourseItem(
            subtask_id = 1,
            course_item_id = 6,
            how_to_exercise_specific = "In this task, we start by modeling a software architecture. We first look at all components as a black box. This creates a content view using an **UML Package diagram**."),
        SubtaskHasCourseItem(
            subtask_id = 1,
            course_item_id = 29,
            how_to_exercise_specific = "Here you have to create a context view. Take a look at the individual components from the documents. How do they hang together? One component could be the OrangeHRM enterprise software, for example."),
        SubtaskHasCourseItem(
            subtask_id = 2,
            course_item_id = 60,
            how_to_exercise_specific = "Here we first consider only the MongoDB database solution. In the following tasks we will also get to know the other components of the MEAN stack."),
        SubtaskHasCourseItem(
            subtask_id = 2,
            course_item_id = 59,
            how_to_exercise_specific = "For this task you have to create collections in a MongoDB. The equivalent of collections would be tables in an SQL database."),
        SubtaskHasCourseItem(
            subtask_id = 2,
            course_item_id = 41,
            how_to_exercise_specific = "Are all four methods of CRUD available in the current solution? This is important in order to be able to fully control the objects."),
        SubtaskHasCourseItem(
            subtask_id = 2,
            course_item_id = 2,
            how_to_exercise_specific = "Here you have to do a round tripping test with JUnit. This means: After you have changed your test objects, the status before the test procedure must be restored. Example: 1. Create a new object. 2. Manipulate the object. 3. Delete the object."),
        SubtaskHasCourseItem(
            subtask_id = 3,
            course_item_id = 42,
            how_to_exercise_specific = "Provide four endpoints for the four CRUD methods. Attention! You also have to use various HTTP methods."),
        SubtaskHasCourseItem(
            subtask_id = 3,
            course_item_id = 39,
            how_to_exercise_specific = "The program you developed last has no API. There are no endpoints through which another (removed) program could reach your program. Now we want to change that via a REST-based API! Take a look at the [tutorial by Niclas Polkow](https://www.youtube.com/watch?v=t64LxbkHVjw), he can explain how to do it. :)"),
        SubtaskHasCourseItem(
            subtask_id = 3,
            course_item_id = 41,
            how_to_exercise_specific = "Provide four endpoints for the four CRUD methods. Attention! You also have to use various HTTP methods."),
        SubtaskHasCourseItem(
            subtask_id = 3,
            course_item_id = 50,
            how_to_exercise_specific = "Create a new request in Postman. Then choose your desired HTTP method. Then you can enter your URL and send the query. For example, if you wanted to get an object with HTTP Get, you can see if it is successful if you get the requested object displayed in the Postman tool."),
        SubtaskHasCourseItem(
            subtask_id = 3,
            course_item_id = 49,
            how_to_exercise_specific = "I recommend that you check out the Swagger documentation for this task."),
        SubtaskHasCourseItem(
            subtask_id = 4,
            course_item_id = 39,
            how_to_exercise_specific = "There are two REST-based APIs in this task: OrangeHRM and OpenCRX. Find out in the course documentation how you can authenticate yourself to be able to send HTTP requests to the two APIs."),
        SubtaskHasCourseItem(
            subtask_id = 4,
            course_item_id = 50,
            how_to_exercise_specific = "Create a new request in Postman. Then choose your desired HTTP method. Then you can enter your URL and send the query. For example, if you wanted to get an object with HTTP Get, you can see if it is successful if you get the requested object displayed in the Postman tool. Important! To carry out the query, you have to authenticate yourself. Check the course documentation for how this works for the two applications OrangeHRM and OpenCRX!"),
        SubtaskHasCourseItem(
            subtask_id = 4,
            course_item_id = 35,
            how_to_exercise_specific = "You can use a UML class diagram for object-oriented analysis. You can also draw relationships such as inheritance, association, aggregation and composition."),
        SubtaskHasCourseItem(
            subtask_id = 4,
            course_item_id = 34,
            how_to_exercise_specific = "Use the UML sequence diagram to show the order in which the authentication steps follow. My tip: Start with the client that calls OrangeHRM or OpenCRX."),
        SubtaskHasCourseItem(
            subtask_id = 5,
            course_item_id = 51,
            how_to_exercise_specific = "It is best to edit a tutorial on Node.js or look at the slides. There you see what you can use to write a simple web server. The slides also contain information about the architecture of Node.js."),
        SubtaskHasCourseItem(
            subtask_id = 6,
            course_item_id = 52,
            how_to_exercise_specific = "Working with JavaScript for the first time is certainly difficult. Therefore we want to see how Java and JavaScript differ. For example, think about object creation. In Java this is done with the new operator. What options does JavaScript offer?"),
        SubtaskHasCourseItem(
            subtask_id = 7,
            course_item_id = 51,
            how_to_exercise_specific = "Get started building a Node.js application. You can find out how to do this on the slides or you can also follow the tutorial from the official website of Node.js."),        
        SubtaskHasCourseItem(
            subtask_id = 7,
            course_item_id = 57,
            how_to_exercise_specific = "Build a Node.js application. Now you have to download and install Express.js as a package via npm. Once you've done that, you can simply use the Express.js component to create different routes. It's best to follow a tutorial on the Express.js official website."),     
        SubtaskHasCourseItem(
            subtask_id = 7,
            course_item_id = 39,
            how_to_exercise_specific = "In this task, we would like to have routes with endpoints for the CRUD methods again. Take a look at how you can use Express.js to specify routes for the various HTTP requests (GET, DELETE etc.)."),     
        SubtaskHasCourseItem(
            subtask_id = 7,
            course_item_id = 50,
            how_to_exercise_specific = "While you are defining the API endpoints, you can already use the Postman tool to test your API. Do you get the correct responses? Pay attention to the different HTTP methods."),     
        SubtaskHasCourseItem(
            subtask_id = 7,
            course_item_id = 35,
            how_to_exercise_specific = "Model all classes and the relationships between them."),     
        SubtaskHasCourseItem(
            subtask_id = 7,
            course_item_id = 32,
            how_to_exercise_specific = "Do you have put all modules in the same folder? Think about useful packages and split your modules. You can then model these using a UML Package Diagram. My tip: How about a separate package for the models?"),     
        SubtaskHasCourseItem(
            subtask_id = 8,
            course_item_id = 26,
            how_to_exercise_specific = "Creates UML diagrams according to the four views. You may have to rework these in the course of your software development."),         
        SubtaskHasCourseItem(
            subtask_id = 8,
            course_item_id = 3,
            how_to_exercise_specific = "How do you plan to integrate your Node.js application with the other two systems OrangeHRM and OpenCRX? You have to use the existing interfaces. You have to write more source code for this! :) Which modules and functions do you need? What should your architecture look like as a whole?"),       
        SubtaskHasCourseItem(
            subtask_id = 10,
            course_item_id = 66,
            how_to_exercise_specific = "Your software did not actually use the MOM architectural style. But we can still apply the patterns to it if we think about the communication at the interfaces."),   
        SubtaskHasCourseItem(
            subtask_id = 10,
            course_item_id = 67,
            how_to_exercise_specific = "This gives you a long list of patterns! Ask me about the individual patterns and I'll tell you more about them."),       
    ]
)

session.commit()
session.close()
