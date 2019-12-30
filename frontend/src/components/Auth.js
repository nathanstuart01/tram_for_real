import { BASE_URL } from './Url';

const user = { access_token: 'token', login: 'False'};

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
    Object.keys(user).forEach(key => {
        localStorage.setItem( key, result[key] );
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
