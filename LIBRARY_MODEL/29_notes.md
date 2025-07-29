develop sequence, collaboration, and class diagrams for the university library management system

Sequence diagram for university library system

```mermaid
sequenceDiagram
    title: Library Management System - Borrow a Book

    actor Student
    actor Librarian
    participant LibrarySystem as Library Management System
    participant Database

    Student->>Librarian: Presents book and library card to borrow

    Librarian->>LibrarySystem: initiateBorrow(studentID, bookID)
    activate LibrarySystem

    %% System checks student status and book availability
    LibrarySystem->>Database: checkStudentStatus(studentID)
    activate Database
    Database-->>LibrarySystem: studentStatus(OK)
    deactivate Database

    LibrarySystem->>Database: checkBookAvailability(bookID)
    activate Database
    Database-->>LibrarySystem: bookStatus(Available)
    deactivate Database

    %% Alt block shows alternative flows for success or failure
    alt Successful Borrow
        LibrarySystem->>Database: updateBookRecord(bookID, 'Borrowed', studentID, dueDate)
        activate Database
        Database-->>LibrarySystem: bookRecordUpdated(Success)
        deactivate Database

        LibrarySystem-->>Librarian: Borrow successful. Due date is [Date].
        Librarian-->>Student: Here is your book. It's due on [Date].

    else Unsuccessful Borrow
        LibrarySystem-->>Librarian: Error: [Reason for failure, e.g., outstanding fines]
        Librarian-->>Student: Sorry, I can't issue this book. [Reason]
    end

    deactivate LibrarySystem

    %% End of sequence diagram



    // develop collaboration diagram for university library system
    collaborationDiagram