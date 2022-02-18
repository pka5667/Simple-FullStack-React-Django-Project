import "./App.css";
import { useState, useEffect } from "react";
import ArticleList from "./components/ArticleList";
import Form from "./components/Form";
import APIService from './components/APIService'
import { useCookies } from "react-cookie";
import {useNavigate} from 'react-router-dom'

function App() {
  const [articles, setArticles] = useState([]);
  const [editArticle, setEditArticle] = useState(null);
  const [cookies, setCookies, removeCookies] = useCookies(['auth_token'])
  let navigate = useNavigate()

  useEffect(() => {
    fetch("http://localhost:8000/api/articles/", {
      method: "GET",
      headers: {
        Authorization: `Token ${cookies['auth_token']}`,
      },
    })
      .then((resp) => resp.json())
      .then((data) => setArticles(data))
      .catch((error) => console.log(error));
  }, []);


  useEffect(() => {
    if(!cookies['auth_token']){
      navigate('/')  // redirects user to the /articles
    }
  }, [cookies])

  const editBtn = (article) => {
    setEditArticle(article);
  };

  const deleteBtn = (article) => {
    APIService.deleteArticle(article.id, cookies['auth_token'])
    const new_articles = articles.filter(myarticle => {
      if(myarticle.id === article.id) return false;
      return true
    })
    setArticles(new_articles)
  }

  const updatedInformation = (article) => {
    const new_article = articles.map((myarticle) => {
      if (myarticle.id === article.id) return article;
      return myarticle;
    });
    setArticles(new_article);
  };

  const insertedInformation = (article) => {
    setArticles([...articles, article])
    setEditArticle(null)
  }

  const articleForm = () => {
    setEditArticle({title:"", description: ''})
  }

  const logoutBtn = () => {
    removeCookies(['auth_token'])
  }

  return (
    <div className="App">
      <div className="row">
        <div className="col">
          <h3>Django And React Js Blog App</h3>
        </div>

        <div className="col">
          <button onClick={articleForm} className="btn btn-primary">Insert Article</button>
        </div>
        <div className="col">
          <button onClick={logoutBtn} className="btn btn-primary">Logout</button>
        </div>
      </div>

      <br />
      <br />
      <ArticleList articles={articles} editBtn={editBtn} deleteBtn={deleteBtn} />

      {editArticle ? (
        <Form article={editArticle} updatedInformation={updatedInformation} insertedInformation={insertedInformation} />
      ) : null}
    </div>
  );
}

export default App;
