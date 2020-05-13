import React from 'react';
import css from './MainPage.module.css';
import { Link } from "react-router-dom";
import "./MainPage.css";


const MainPage = (props) => {
    const url = "https://oauth.vk.com/authorize?client_id=7462552&redirect_uri=https://voting-school47.herokuapp.com/user/login&scope=12&display="

    console.log(props.match.params.id)

    let auth = props.auth
    return (
        <div className={css.container}>
            <div className={css.img}></div>
            <div className={css.btn}>
                <span></span>
                <span></span>
                <span></span>
                <span></span>
                {auth?
                    <Link className={css.main_link} to="/candidates">проголосовать</Link>
                :
                    <a href={url} className={css.main_link}>авторизироваться</a>
                }
                </div>
        </div>
    );
}

export default MainPage;