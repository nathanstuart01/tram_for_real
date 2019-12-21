export const login = (result) => {
    localStorage.setItem('token', result);
}

export const logout = () => {
    localStorage.removeItem('token');
}