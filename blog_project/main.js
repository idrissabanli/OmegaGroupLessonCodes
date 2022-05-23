document.addEventListener("DOMContentLoaded",  function(){
    let blogSection = document.getElementById('blogs')
    async function renderBlogs(){
        console.log('here');
        let response = await fetch('http://localhost:8000/api/stories/', {
            headers: {
                'Content-Type': 'application/json',
                },
            method: "GET",
        });
        let data = await response.json()
        // console.log(data);
        
        for(let blog of data){
            blogSection.innerHTML += `
            <div class="col-4 mb-4">
                <div class="card" >
                    <img src="${blog.image}" class="card-img-top " alt="...">
                    <div class="card-body">
                      <h5 class="card-title">${blog.title}</h5>
                      <p class="card-text">${blog.content}</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
            `;
        }
    }
    renderBlogs();
});
