import React, {useState, useEffect} from 'react'
import APIService from '../components/APIService'
import { useCookies } from "react-cookie";

export default function Form(props) {

    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [token] = useCookies(['auth_token'])

    useEffect(() => {
        setTitle(props.article.title)
        setDescription(props.article.description)
    }, [props.article])

    const updateArticle = ()=>{
        APIService.UpdateArticle(props.article.id, {title, description}, token['auth_token'])
        .then(resp => props.updatedInformation(resp))
    }

    const insertArticle = ()=>{
        APIService.InsertArticle({title, description}, token['auth_token'])
        .then(resp => props.insertedInformation(resp))
    }

  return (
    <div>
        {props.article && (
            <div className="mb-3">
                <label htmlFor="title" className="form-label">Title</label>
                <input type="text" className="form-control" id="title" placeholder="Please enter the title" value={title} onChange={e=>setTitle(e.target.value)}/>

                <label htmlFor="description" className="form-label">Description</label>
                <textarea name="" className="form-control" id="description" cols="30" rows="5" value={description} onChange={e=>setDescription(e.target.value)} placeholder="Please enter the description"></textarea>
                <br />

                {
                    props.article.id ? <button className="btn btn-success" onClick={updateArticle}>Update Article</button>
                    : <button className="btn btn-success" onClick={insertArticle}>Add Article</button>
                }
                
            </div>
        )}
    </div>
  )
}
