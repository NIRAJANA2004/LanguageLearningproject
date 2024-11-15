import axios from "axios";

const API_URL = "http://localhost:5000/api";

export const getLessons = async () => {
    const response = await axios.get(`${API_URL}/lessons`);
    return response.data;
};

export const getUserProgress = async (userId) => {
    const response = await axios.get(`${API_URL}/users/${userId}/progress`);
    return response.data;
};

export const updateProgress = async (userId, lessonId, progress) => {
    const response = await axios.put(`${API_URL}/users/${userId}/progress`, {
        lesson_id: lessonId,
        progress: progress,
    });
    return response.data;
};
