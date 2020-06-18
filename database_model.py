import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, backref
import sqlalchemy.dialects.postgresql as sql


eng = create_engine("postgresql+psycopg2://postgres:admin@/chatbot")

Base = declarative_base()

class LectureHasCourseItem(Base):
    __tablename__ = 'lecture_has_course_item'
    lecture_id = Column(Integer, ForeignKey('lecture.id'), primary_key=True)
    course_item_id = Column(Integer, ForeignKey('course_item.id'), primary_key=True)

class SubtaskHasCourseItem(Base):
    __tablename__ = 'subtask_has_course_item'
    subtask_id = Column('subtask_id', Integer, ForeignKey('subtask.id'), primary_key=True)
    course_item_id = Column('course_item_id', Integer, ForeignKey('course_item.id'), primary_key=True)

class File(Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    data = Column(sql.BYTEA)

class CourseItem(Base):
    __tablename__ = "course_item"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    how_to = Column(String)
    link = Column(String)
    image_id = Column(Integer, ForeignKey('file.id'))
    image = relationship(
        "File",
        backref=backref("course_items",
                        uselist=True,
                        cascade='delete,all',
                        passive_deletes=True))

class Lecture(Base):
    __tablename__ = "lecture"
    id = Column(Integer, primary_key=True)
    chapter = Column(Integer)
    title = Column(String)
    file_id = Column(Integer, ForeignKey('file.id', ondelete='CASCADE'))
    file = relationship(
        "File",
        backref=backref("lectures",
                        uselist=True,
                        cascade='delete,all'))              
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
    course_items = relationship(
        "CourseItem",
        secondary='subtask_has_course_item',
        backref="subtasks")

Base.metadata.bind = eng      
Base.metadata.drop_all()
Base.metadata.create_all()        
        
DBSession = sessionmaker(bind=eng)
session = DBSession()   

# Add course items
list_course_items = [
        CourseItem(
            id = 1,
            title = 'System design',
            description = 'System design is the process of defining the architecture, modules, interfaces, and data for a system to satisfy specified requirements.',
            how_to = None,
            link = 'https://en.wikipedia.org/wiki/Systems_design',
            image_id = None),
        CourseItem(
            id = 2,
            title = 'Unit testing',
            description = 'In computer programming, unit testing is a software testing method by which individual units of source code, sets of one or more computer program modules together with associated control data, usage procedures, and operating procedures, are tested to determine whether they are fit for use.',
            how_to = None,
            link = 'https://en.wikipedia.org/wiki/Unit_testing',
            image_id = None), 
        CourseItem(
            id = 3,
            title = 'Integration architecture',
            description = 'There are multiple definitions for Integration architecture but here is one by Professor Alda: An integration architecture defines **global design decisions** for the integration of potentially *distributed* and *heterogeneous* software components. An integration architecture also makes **implications for tools and frameworks** for developing, testing, andmaintaining *interoperable* software.',
            how_to = None,
            link = None,
            image_id = None), 
        CourseItem(
            id = 4,
            title = 'Architectural styles',
            description = 'Software architecture styles define rules and assumptions for a type (template, class) of software architectures. That means, that the concrete  implementation of a software architecture of a software is an instance of a software architecture style. Here I have an example of the Layer pattern for you:',
            how_to = None,
            link = None,
            image_id = None), # 'http://www.ruanyifeng.com/blogimg/asset/2016/bg2016090302.png'
        CourseItem(
            id = 5,
            title = 'Architectural patterns',
            description = 'Software architecture styles define rules and assumptions for a type (template, class) of software architectures. That means, that the concrete  implementation of a software architecture of a software is an instance of a software architecture style. Here I have an example of the Layer pattern for you:',
            how_to = None,
            link = None,
            image_id = None), # 'http://www.ruanyifeng.com/blogimg/asset/2016/bg2016090302.png'),
        CourseItem(
            id = 6,
            title = 'Software Architecture',
            description = 'A software architecture describes the decomposition of a software system that follows the specifications of pertaining architectural styles. The description of a software architecture comprises the following constituting elements: The fundamental **architecture elements** and their **interfaces**, the **interaction relationships** among those architecture elements as well as the **architecture directives**, and the characteristic **factors describing the economic value** of the whole software architecture.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 7,
            title = 'Architecture elements',
            description = 'The architecture elements describe atomic units (e.g. classes, modules) and complex units (e.g. subsystems, packages) of a software architecture.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 8,
            title = 'Interaction relationships',
            description = 'Architecture elements have to interact with each other. The easiest way is probably the local interaction via a local method call. But there are also more advanced models like the Observer Pattern.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 9,
            title = 'Non-blocking asynchronous interaction',
            description = 'Non-blocking or asynchronous interaction: The sender is not blocked, may receive or initiate further requests; stays responsive. Notification e.g., by a callback function.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 10,
            title = 'Blocking synchronous interaction',
            description = 'Blocking or synchronous interaction: The sender remains blocked, has to await the answer (response).',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 11,
            title = 'Conway\'s law',
            description = 'Conway\'s Law says: \'Organizations which design systems [...] are constrained to produce designs which are copies of the communication structures of these organizations.\' Let\'s interpret that: The software architecture of a system is influenced by formal and informal organizational structures.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 12,
            title = 'Architecture directives',
            description = 'Architecture Directives are additional properties, rules, and restrictions on a software architecture that cannot be directly inferred by the decomposition of the software, for instance quality control or design of security aspects.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 13,
            title = 'Economic value',
            description = 'Characteristic factors for describing the economic value are usually identified on a business level, but are evaluated on an architectural level at runtime. Examples: SLA (contractual agreement between client und provider) and KPI (functional measurements that can be extracted during runtime).',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 14,
            title = 'SLA',
            description = 'Characteristic factors for describing the economic value are usually identified on a business level, but are evaluated on an architectural level at runtime. Examples: SLA (contractual agreement between client und provider) and KPI (functional measurements that can be extracted during runtime).',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 15,
            title = 'KPI',
            description = 'Characteristic factors for describing the economic value are usually identified on a business level, but are evaluated on an architectural level at runtime. Examples: SLA (contractual agreement between client und provider) and KPI (functional measurements that can be extracted during runtime).',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 16,
            title = 'Legacy system',
            description = 'A legacy system is an old computer system or application program, which is still in use. Often referencing a system as legacy means that it paved the way for the standards that would follow it. This can also imply that the system is out of date or in need of replacement.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 17,
            title = 'API',
            description = 'An application programming interface (API) is a computing interface which defines interactions between multiple software intermediaries. It defines the kinds of calls or requests that can be made, how to make them, the data formats that should be used, the conventions to follow, etc.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 18,
            title = 'Monolithic architecture',
            description = 'There is no separation of application logic, data storage, and user interface (e.g., Mainframe-Batch programs).',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 19,
            title = 'Data transfer',
            description = 'Data transfer is a basic concept of integration: An application writes into a file, while another application reads from the same after a while.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 20,
            title = 'Shared database',
            description = 'The shared database is a basic concept of integration: Various systems use a global databasefor sharing data.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 21,
            title = 'Methods calls',
            description = 'Method calls are a basic concept of integration: A system provides an API that can be accessed by Remote Procedure Calls (RPC) in a synchronous way.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 22,
            title = 'Messaging',
            description = 'Messaging is a basic concept of integration: A system sends messages to common message channel in an asynchronousway. Receiver component can read the message later on.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 23,
            title = 'Point-to-Point',
            description = 'Point-to-Point is a basic integration pattern: There is a direct connection of the corresponding interfaces.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 24,
            title = 'Hub and Spoke',
            description = 'Hub and Spoke is a basic integration pattern: All systems were integrated from a single location, the hub. The state is maintained in a shared database and there is only a single point of integration and transformation.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 25,
            title = 'Bus',
            description = 'A Bus is a basic integration pattern: Adapters are used for transformation. There is no state maintained and add-on services such as routing required.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 26,
            title = '4 Views Model',
            description = 'The 4 Views Model includes the modelling of the environment of the system under development, indicating the most relevant dependencies. It consists of four views: **Context view**, **runtime view**, **module view** and **distribution view**.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 27,
            title = 'Module view',
            description = 'The Module View is part of the **4 Views Model** and it models static structures of the architecture elements of the system, subsystems, components, classes and their interfaces. It represents the dependencies among these elements. For representation, **UML Component Diagrams**, **UML Package Diagrams** and **UML Class Diagrams** were used.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 28,
            title = 'Runtime View',
            description = 'The Runtime View is part of the **4 Views Model** and describes, which architecture elements (classes, objects, subsystems, components,…) of a systems do exist at runtime and how they interact together (dynamic perspective). Actors can also be included, too. For representation, **UML Sequence Diagrams** were used.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 29,
            title = 'Context View',
            description = 'The Context View is part of the **4 Views Model** and models the environment of the system under development, indicating the most relevant dependencies. It is the abstract modelling of the system as a black box to the neighboring system (no internal structure is to be revealed). For representation, **UML Package Diagrams** were used.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 30,
            title = 'Distribution View',
            description = 'The Distribution View is part of the **4 Views Model** and it describes the runtime environments of the system in terms of hardware devices (e.g., server network, firewalls) and the corresponding protocolls. It also represents the  execution environments (e.g., application server, container). For representation, **UML Distribution Diagrams** were used.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 31,
            title = 'UML Component Diagram',
            description = 'An UML Component Diagram represents the architecture elements (subsystems, components) of a system as organized during runtime. The interfaces were modelled explicitly (required and provided) and the components were modelled as white boxes with dedicated connections from internal implementations to external interfaces. The UML Component Diagram is used for the **Module View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 32,
            title = 'UML Package Diagram',
            description = 'Package Diagrams show an overview of the decomposition of the complete system in packages and subsystems. They were used for the **Context View** and the **Module View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 33,
            title = 'UML Distribution Diagram',
            description = 'An UML Distribution Diagram represents the hardware topology as well as the distribution of the software to the hardware. It is used for the **Distribution View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 34,
            title = 'UML Sequence Diagram',
            description = 'A sequence diagram shows object interactions arranged in time sequence. It depicts the objects and classes involved in the scenario and the sequence of messages exchanged between the objects needed to carry out the functionality of the scenario. It is used for the **Runtime View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 35,
            title = 'UML Class Diagram',
            description = 'A Class Diagram is a type of static structure diagram that describes the structure of a system by showing the system\'s classes, their attributes, operations (or methods), and the relationships among objects. It is used for the **Module View** of the **4 Views Model**.',
            how_to = None,
            link = None,
            image_id = None),
        CourseItem(
            id = 36,
            title = 'Layer Pattern',
            description = 'The Layer Pattern is the decomposition of system functionality in single layers: Presentation Layer, Application Layer, Domain Layer and Infrastructure Layer.  Each layer implements a coherent functionality block on a given abstraction level and provides services for the lower layers (or same level). Each layer can be developed, deployed, and maintained independently.',
            how_to = None,
            link = None,
            image_id = None)
    ]
session.add_all(list_course_items)

# Add lectures
session.add_all(
    [
        Lecture(
            id = 1,
            chapter = 1,
            title = 'Introduction and Organization, First View on Integration Architecture',
            file_id =  None),
        Lecture(
            id = 2,
            chapter = 2,
            title = 'Introduction to Software Architectures and Architectural Integration',
            file_id = None), 
        Lecture(
            id = 3,
            chapter = 2,
            title = 'Introduction to Software Architectures and Architectural Integration',
            file_id = None), 
        Lecture(
            id = 4,
            chapter = 2,
            title = 'Introduction to Software Architectures and Architectural Integration',
            file_id = None), 
        Lecture(
            id = 5,
            chapter = 3,
            title = 'A deeper look on Architectural Integration: Solutions and Patterns',
            file_id = None), 
        Lecture(
            id = 6,
            chapter = 4,
            title = 'Patterns and Tools for Interface Integration Testing',
            file_id = None), 
        Lecture(
            id = 7,
            chapter = 5,
            title = 'Message-Oriented Middleware (MOM) –StateOf-The-Art solutions',
            file_id = None) 
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
            course_item_id = 1),
        SubtaskHasCourseItem(
            subtask_id = 1,
            course_item_id = 2
        )
    ]
)

session.commit()
session.close()
