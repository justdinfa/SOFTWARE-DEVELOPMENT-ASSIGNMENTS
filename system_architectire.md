THE OSI MODEL
The OSI Model also known as Open System Interconnection Model. IT is a conceptual framework created by the International Organization for Standardization (ISO) to describe or explain how data is transmitted across a network using a structured seven-layer architecture.
what it does is that:
1. Divides network communication into seven functional layers.
2. Assigns specific responsibilities to each layer.
3. Promotes compatibility between different networking systems.
4. Simplifies network design, implementation, and troubleshooting.
 
 THE LAYERS OF OSI MODELS
 1. Layer 1: The Physical Layer
The Physical Layer is the foundation of the OSI model, acting as the bridge for actual physical connections between devices. Its primary mission is the transmission of raw, unstructured bitstreams over a physical medium from one node to the next.
- Responsibility: it translates physical signals back into digital 0's and 1's to be processed by the dataq link layer.
- Hardware: Common devices operating at this level include Hubs, Repeaters, Modems, and Cables.
- Bit Synchronization: It ensures the sender and receiver are "in sync" by providing a clock signal that controls the timing of bit transmission.
- Bit Rate Control: It dictates the transmission speed, defined as the number of bits sent per second.
- Physical Topologies: It defines the structural layout of the network, such as Bus, Star, or Mesh configurations.
- Transmission Mode: It determines the direction of data flow, utilizing modes like Simplex (one-way), Half-Duplex (two-way, one at a time), or Full-Duplex (simultaneous two-way).

2. Layer 2: The Data Link Layer (DLL)
The Data Link Layer serves as the bridge between the physical hardware and the logical network, ensuring reliable node-to-node delivery of data. Its primary goal is to ensure that data transfer is error-free across the physical medium.

- Data Packaging (Framing): At this layer, data packets received from the Network layer are divided into manageable units called Frames. This is done by adding specific "start" and "stop" bits so the receiver can recognize where one unit of data ends and the next begins.

- Addressing and Hardware: The DLL uses MAC addresses (Physical Addressing) to identify hosts. It encapsulates the senders and receivers MAC addresses into the frame header. Common devices operating here are Switches and Bridges.

- Sublayers:
* Logical Link Control (LLC): Manages flow and error control while acting as an interface for upper-layer protocols.
* Media Access Control (MAC): Determines how devices physically access the transmission medium and handles hardware addressing.
-  Error Control: It detects and retransmits damaged or lost frames to maintain data integrity.

-  Flow Control: It synchronizes the data rate between a fast sender and a slower receiver to prevent data "bottlenecks" or loss.

-  Access Control: When multiple devices share the same communication channel, the MAC sublayer dictates which device has the right to transmit at any given time to avoid collisions.

3. Layer 3: The Network Layer
The Network Layer manages data transmission between hosts across different networks by handling logical addressing and path finding.

- Data Unit: Data segments are encapsulated into Packets.
- Logical Addressing: Assigns unique IP addresses (sender and receiver) to the packet header to identify devices globally.
- Routing: Determines the most efficient physical path from the source to the destination across interconnected networks.
- Hardware: Primarily implemented via Routers and Switches.
- Inter-networking: Facilitates communication between disparate networks by directing traffic to the correct destination.

4. Layer 4: The Transport Layer
The Transport Layer ensures the end-to-end delivery of entire messages. It acts as a liaison, providing services to the Application layer while utilizing the infrastructure of the Network layer to ensure data reaches the correct application on the destination host.

- Data Unit: Data is broken down into Segments.
- Service Point Addressing: Uses Port Numbers (e.g., Port 80 for web traffic) to ensure data is delivered to the specific process or application intended, not just the device.
- Segmentation & Reassembly: Splits large messages into smaller segments for transmission and reassembles them in the correct order at the destination.
- Protocols: Common protocols include TCP (reliable), UDP (fast).
- Connection-Oriented (TCP): Requires a "handshake" to establish a connection; ensures reliability via error checking and acknowledgements.
- Connectionless (UDP): Sends data immediately without a formal connection; faster but offers no guarantee of delivery.

5. Layer 5: The Session Layer
The Session Layer acts as the "dialogue manager," governing the opening, closing, and security of communication channels between two devices.

- Session Lifecycle: Manages the establishment, maintenance, and termination of connections between applications.
- Authentication & Security: Ensures that the communicating parties are verified and the connection is secure.
- Synchronization: Inserts checkpoints into the data stream. This allows a transfer to resume from the last saved point if a failure occurs, rather than restarting from the beginning.
- Dialog Control: Directs whether communication is half-duplex (alternating) or full-duplex (simultaneous).
- Practical Example: In a web-based messenger, the Session Layer maintains the active link between your browser and the server, ensuring your specific chat remains open and synchronized while handling background encryption and data conversion.

6. Layer 6: The Presentation Layer
Often called the Translation Layer, the Presentation Layer ensures that data is formatted, secured, and compressed so that the receiving application can correctly interpret it.

- Translation: It extracts data from the Application Layer and converts it into a standardized format for network transmission, bridging differences in data representation between different systems.
- Standards & Formats: Handles the encoding of media using standards such as JPEG, MPEG, and GIF.
- Encryption/Decryption: Provides security by converting "plain text" into "ciphertext" (encryption) and back again (decryption) using key values. This process is typically handled by protocols like TLS/SSL.
- Compression: Reduces the total number of bits required for transmission, which increases network efficiency and speed.

7. Layer 7: The Application Layer
The Application Layer sits at the top of the OSI stack and serves as the direct interface between the software user and the network. It produces the data that will be sent and displays the information received from other layers.

- User Interface: Acts as a "window" for network-based applications (like web browsers or email clients) to access network services.
- Core Protocols: Utilizes high-level protocols such as HTTP/S (Web), SMTP (Email), FTP (File Transfer), and DNS (Domain Name Resolution).
- Network Virtual Terminal (NVT): Enables users to log into and interact with remote hosts as if they were physically present at the terminal.
- File Transfer, Access, and Management (FTAM): Provides the framework for users to retrieve, manage, and manipulate files stored on remote computers.
- Directory Services: Offers distributed database access to manage global information regarding various network objects and services.

IN A NUTSHELL,
Application Layer: it's where Applications create the data.
Presentation Layer:  it's where Data is formatted and encrypted.
Session Layer: here, Connections are established and managed.
Transport Layer: Data is broken into segments for reliable delivery.
Network Layer: Segments are packaged into packets and routed.
Data Link Layer: Packets are framed and sent to the next device.
Physical Layer: Frames are converted into bits and transmitted physically.

REASONS WHY OSI MODELS LAYERS ARE NOT USED IN REAL WORLD PRODUCTION

The OSI model layers are not widely used in real-world production due to these following reasons:
- Complexity and Implementation: The OSI model's complexity made initial implementations hard, slow, and expensive compared to simpler alternatives. 
- Redundant Layers: Some layers, particularly the session and presentation layers, have minimal functionality in practical deployments, adding unnecessary overhead. 
- Service Duplication: Multiple layers offer similar services like addressing, flow control, and error control, leading to redundancy and inefficiency. 
- Practical Solutions: The OSI standards remain largely theoretical and do not provide sufficient solutions for practical network implementation challenges. 
- Industry Resistance: The model faced significant resistance from the academic and professional community, who viewed it as an inferior alternative to the proven TCP/IP model.
 
 THE MODELS THAT ARE USUALLY USED AND ITS OWN LAYERS ARE
 THE TCP/IP MODEL
 - APPLICATION LAYER
 - TRANSPORT LAYER
 - INTERNET LAYER
 - NETWORK LAYER

 THE WHOLE PROCESS THAT GOES ON FROM WHEN YOU PERFORM AN ACTION ON YOUR SYSTEM FROM THE GUI ALL THE WAY DOWN TO YOUR KERNEL, MEMORY, ADDRESSING MODES ETC AND BACTO THE GUI:
Step 1 — Boot Process: Where Everything Starts
The boot process marks the first stage of how an operating system works when a computer powers on. At this moment the machine contains inactive hardware components and stored system software, but nothing has begun executing yet.

During this stage the boot process operating system workflow transitions from hardware initialization to loading the system kernel into memory. Every modern system follows a similar structure, whether it runs the windows operating system or relies on the linux boot process used by many servers and development environments.

Two major phases occur during this stage: hardware initialization and operating system loading.

Power On and POST
When a computer receives electrical power, the processor immediately begins executing firmware instructions stored on the motherboard. These instructions belong to system firmware such as BIOS or UEFI.

The first responsibility of this firmware is hardware verification through the Power-On Self-Test. POST checks whether essential components such as RAM, CPU, and storage devices respond correctly.

Memory modules undergo quick validation tests. Storage controllers are identified. Input devices such as keyboards become available for early system commands. If a critical component fails during POST, the firmware halts the startup sequence and signals an error.

This stage is crucial to operating system architecture. The OS cannot function until the hardware environment is stable and ready for software execution. Firmware ensures that the processor, memory, and storage devices are operational before transferring control to the next stage.

Once hardware initialization completes successfully, the firmware searches for a bootable device. That device usually contains the bootloader responsible for loading the operating system itself.

Bootloader and OS Loading
After locating a valid boot device, firmware transfers control to the system bootloader. The bootloader is a small program designed specifically to locate and load the operating system kernel from storage.

According to GeeksforGeeks, booting is the process that starts when a computer is powered on and loads the operating system from secondary storage into RAM so it can manage hardware and software operations.

This step explains the significance of the bootloader. The OS cannot execute directly from disk storage. It must first be placed into main memory so the processor can access instructions rapidly.

During this phase the bootloader identifies the system kernel file, loads it into RAM, and prepares the parameters required for startup. Configuration information such as hardware settings and startup options may also be passed to the kernel.

The process remains consistent across platforms. The windows operating system uses a boot manager that loads the Windows kernel. Linux systems rely on bootloaders such as GRUB, which performs the same task for the Linux kernel.

Once the kernel enters memory and begins execution, the computer transitions from firmware control to the main operating system environment.

Step 2 — Kernel Initialization (The Brain of the OS)
After the bootloader finishes its job, the system kernel begins executing. This stage marks a major turning point in how an operating system works, since the kernel now assumes full control over hardware resources.

The kernel forms the core component responsible for managing CPU scheduling, memory allocation, and hardware communication. Every modern OS relies on this layer to maintain stability and coordinate system activity.

These responsibilities define the operating system kernel as the central control structure inside the system. All applications and services ultimately rely on it to access hardware safely.

How the Kernel Loads into Memory
Kernel execution begins immediately after the bootloader loads it into memory. At this moment the processor starts running the kernel’s initialization routines.

Based on Baeldung, the boot loader’s primary job is to locate the operating system kernel on disk, load it into memory, and execute it with the required parameters.

Once the kernel starts running, it begins setting up essential subsystems. Memory management structures are created, device drivers begin initializing, and interrupt handling mechanisms become active.

These steps illustrate how operating systems work internally. Instead of running applications immediately, the system first establishes a controlled environment where processes can execute safely.

Many responsibilities occur during this phase. The kernel identifies available hardware devices, initializes low-level drivers, and prepares scheduling systems that will later distribute processor time among running programs.

These initialization routines are fundamental to os resource management. Without them, multiple programs would compete for hardware access and cause system instability.

The kernel also prepares the internal structures that define kernel in operating system design. These structures track running processes, memory allocation, and device activity.

Modern systems such as the microsoft windows operating system and Linux implement similar initialization stages, although their internal implementations differ.

Kernel Mode vs User Mode
A key principle of operating system architecture appears during kernel initialization: the separation between kernel mode and user mode.

Kernel mode provides full access to hardware and system memory. Only the OS kernel and trusted system components operate within this privileged environment.

User mode operates under strict restrictions. Applications run in this environment to prevent them from directly accessing hardware or critical memory regions.

This separation protects system stability. If an application crashes or attempts invalid operations, the failure remains isolated within user mode rather than affecting the entire system.

Privilege rings within modern processors enforce this structure. The kernel operates at the highest privilege level, while applications run at lower privilege levels.

These protections illustrate how an OS functions as both a resource manager and a stability mechanism. The kernel controls hardware access while ensuring that applications cannot interfere with critical system operations.

Once these protections and core services are established, the operating system becomes ready to begin managing processes and executing applications.

Step 3 — Process Management and CPU Scheduling
Once the kernel finishes initialization, the system becomes ready to execute programs. Applications can launch, background services begin running, and the processor starts handling multiple tasks simultaneously. This stage reveals another critical aspect of how an operating system works.

A computer rarely runs a single program at a time. Web browsers, system services, messaging tools, and background utilities may all operate concurrently. Managing this activity falls under process management in operating system design.

Each running program becomes a process. The OS tracks these processes using internal data structures that store execution state, memory usage, and priority information. These structures allow the system to pause one task, switch to another, and resume execution later without losing progress.

This behavior defines a multitasking operating system. The system creates the illusion that many programs run at the same time even though the processor executes only one instruction stream at any given moment.

Efficient os resource management ensures that processor time is distributed fairly across active tasks. Without scheduling control, a single application could monopolize the CPU and make the system unresponsive.

The mechanism responsible for this coordination is the scheduler.

How the Scheduler Manages Multiple Tasks
The scheduler determines which process receives CPU time and for how long. It evaluates active processes, assigns time slices, and performs context switches that allow the processor to move between tasks.

This mechanism plays a central role in how OS works during everyday computing. Each program receives a small execution window called a time slice. When that slice expires, the scheduler pauses the process and selects another task waiting in the queue.

Time slicing allows dozens of programs to operate smoothly even on a single processor core. The rapid switching happens so quickly that users perceive all tasks as running simultaneously.

Context switching is another essential operation in this stage. When the system pauses a process, it saves the current processor state including registers, program counters, and memory references. Later, the scheduler restores this state so the program continues from the exact point where it stopped.

This coordination highlights core operating system functions. The OS balances responsiveness, fairness, and efficiency while distributing limited CPU resources among many competing tasks.

Different workloads require different scheduling strategies. Systems designed for servers may prioritize throughput, while desktop systems emphasize responsiveness to user input.

CPU Scheduling Algorithms
Operating systems implement several algorithms to determine how processes receive CPU time. These algorithms influence system responsiveness and overall performance.

Algorithm	How It Works	Best Use Case
FCFS	First come first served	Simple workloads
Round Robin	Time slicing	Multitasking
Priority	Based on importance	Critical tasks
First-Come First-Served scheduling executes tasks in the order they arrive. The method is simple but can cause long wait times if large processes occupy the processor.

Round Robin scheduling improves responsiveness by assigning equal time slices to processes. After a slice ends, the scheduler rotates to the next process in the queue. This strategy works well in multitasking environments.

Priority scheduling assigns CPU time based on process importance. Critical system services may receive higher priority while background tasks receive less frequent execution.

These strategies demonstrate another dimension of how an operating system works. The OS constantly evaluates workloads, balancing performance and responsiveness across the entire system.

Step 4 — Memory Management and Virtual Memory
Every running process requires memory to store instructions and active data. Managing this memory efficiently forms another core responsibility of the OS.

The memory management in operating system subsystem controls how RAM is allocated, tracked, and protected during program execution. Without structured management, programs could overwrite each other’s data and cause system instability.

When an application starts, the OS assigns a dedicated memory space. This isolation ensures that each program operates independently without interfering with others.

Effective ram management also determines how much memory each process receives. Systems with limited RAM must allocate resources carefully to prevent performance issues.

Virtual memory introduces another layer of flexibility. Instead of relying solely on physical RAM, the OS can extend available memory using storage devices.

The concept plays an important role in how OS works when multiple programs run simultaneously. When RAM becomes full, the OS temporarily moves inactive memory pages to a disk-based area known as the swap space or page file.

This process, known as paging, allows the system to maintain application stability even under heavy workloads. Active processes remain in RAM while less frequently used data moves to secondary storage.

Although accessing disk storage is slower than RAM, virtual memory prevents applications from failing due to memory shortages.

These techniques demonstrate how operating system architecture balances efficiency and reliability. Memory management ensures that programs receive the resources they need without compromising system stability.

Step 5 — File System and Storage Handling
Persistent data storage forms another major responsibility of the OS. Applications constantly read files, save documents, and access system resources stored on disks or solid-state drives.

The file system in operating system design organizes this data into structured directories and files. Without this structure, locating or modifying information would become extremely difficult.

Every file operation follows a structured flow. When an application requests data, the OS translates that request into storage instructions. The storage controller retrieves the required blocks, and the OS returns the data to the requesting program.

This process illustrates another part of how operating systems work during everyday computing. The OS acts as an intermediary between software and storage hardware.

Storage coordination also includes permissions and access control. Users and applications receive defined privileges that determine which files they can read or modify.

Modern computer operating systems use different file system technologies depending on their design goals. Windows commonly uses NTFS, while Linux systems rely on file systems such as ext4.

Although the implementations differ, the core concept remains the same. The OS manages storage access, organizes data structures, and ensures consistent file operations across the system.

These storage mechanisms support efficient storage management, allowing applications to store and retrieve information without directly interacting with hardware devices.

Step 6 — Device Drivers and Hardware Communication
Hardware devices such as keyboards, printers, graphics cards, and network adapters require specialized software to interact with the operating system. This interaction occurs through device drivers.

Drivers provide an abstraction layer that allows applications to communicate with hardware without needing to understand device-specific details. This abstraction plays a central role in device management operating system design.

Each hardware device exposes capabilities through driver interfaces. The OS communicates with these drivers using structured commands that translate software requests into hardware operations.

These interactions often rely on system call in operating system mechanisms. Applications issue system calls when they need to perform actions that require kernel access, such as reading from storage or sending network data.

Drivers interpret these requests and forward them to the appropriate hardware components.

This architecture demonstrates how an OS functions as the communication hub between software and physical devices. Applications operate at a high level, while the OS manages low-level hardware interaction.

A simple keyboard input illustrates the process clearly. When a user presses a key, the keyboard hardware sends a signal to the system. The keyboard driver interprets the signal, and the OS forwards the resulting character to the active application.

This layered approach ensures compatibility across diverse hardware devices while maintaining system stability and security.

Through device drivers, the operating system maintains consistent communication with hardware components while protecting the core system from direct application access.
