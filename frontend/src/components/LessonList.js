import React, { useEffect, useState } from "react";
import { getLessons } from "../api/api";

const LessonList = () => {
    const [lessons, setLessons] = useState([]);

    useEffect(() => {
        const fetchLessons = async () => {
            const data = await getLessons();
            setLessons(data);
        };
        fetchLessons();
    }, []);

    return (
        <div>
            <h2>Lessons</h2>
            <ul>
                {lessons.map((lesson) => (
                    <li key={lesson.id}>
                        <h3>{lesson.title}</h3>
                        <p>{lesson.content}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default LessonList;
