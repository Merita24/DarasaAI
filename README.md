# DarasaAI – AI Classroom Assistant for Last-Mile Schools

## Overview

DarasaAI is an AI-powered classroom assistant designed for **last-mile schools where devices are limited and teachers are scarce**. The system enables a **single-device classroom** to deliver lessons, quizzes, explanations, and voice learning support using AI.

DarasaAI works in **both online and offline environments**, making it suitable for schools with unstable or limited internet access.

The system integrates:

* AI-generated lessons and quizzes
* Voice explanations for students
* WhatsApp chatbot interaction
* Offline CLI interface for low-connectivity environments

This allows students and educators to access educational support **anytime, even in resource-constrained classrooms**.

---

# Problem

Many schools in rural or under-resourced regions face:

* **Device scarcity** – often only one device for an entire classroom
* **Teacher shortages** – not enough educators for all subjects
* **Limited internet connectivity**
* **Limited access to learning resources**

DarasaAI helps address these issues by acting as an **AI teaching assistant** capable of generating learning materials on demand.

---

# Key Features

## AI Lesson Generator

Generates structured educational lessons for a given topic.

Example:

```
POST /lesson/start
```

Students or teachers can request lessons for specific topics and grade levels.

---

## Quiz Generator

Creates quizzes based on lesson content to help reinforce learning.

Students can also request quizzes via the API or WhatsApp.

---

## AI Explanations

Students can ask questions and receive AI-generated explanations.

Example commands:

```
explain photosynthesis
```

---

## Voice Explanations

Text explanations can be converted into **audio learning content** using OpenAI text-to-speech.

Audio files are generated and served through:

```
/audio/{filename}.mp3
```

This helps support:

* audi
