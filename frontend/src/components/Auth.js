import { BASE_URL } from './Url';

const user = { client: 'client', email: 'email', token: 'token', nickname: 'nickname'};

export const authenticatedUser = () => {
    let currentUser = {};
    Object.keys(user).forEach(key => {
        let entry = localStorage[key];
        if(entry)
            currentUser[key] = entry;
    });
    return currentUser;
}

export const login = (result) => {
    console.log(result);
    console.log(user)
    Object.keys(user).forEach(key => {
        debugger
        localStorage.setItem( user[key], result[key] );
    });
}

export const logout = () => {
    Object.keys(user).forEach(key => {
        localStorage.removeItem(key);
    })
}

export const auth = (user, endpoint, cb) => {
    fetch(`${BASE_URL}/${endpoint}`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({...user})
        }).then(res => res.json())
            .then( result => {
                if (result['login'] === true) {
                    login(result)
                }
                else {
                    console.log('Invalid login credentials');
                }
            })
            .then( () => cb() )
            .catch( error => {
                console.log(error.message);
            })
        }
