function ajaxSend(url, params) {
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencocded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error));
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    e.preventDefault();
    let url = this.getAttribute("action");
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    let template = Hogan.compile(html);
    let output = template.render(data);
    const div = document.querySelector('.left-ads-display>.row');
    div.innerHTML = output;
}

let html = '\
{{#movies}}\
 <div class="col-md-3 product-men">\
   <div class="product-shoe-info editContent text-center mt-lg-4">\
       <div class="men-thumb-item">\
           <img src="media/{{poster}}" class="img-fluid" alt="">\
       </div>\
       <div class="item-info-product">\
           <h4 class="">\
               <a href="detail/{{ url }}" class="editContent">\
                   {{ title }}\
               </a>\
           </h4>\
           <ul class="stars">\
               <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a>\
               </li>\
               <li><a href="#"><span class="fa fa-star" aria-hidden="true"></span></a>\
               </li>\
               <li><a href="#"><span class="fa fa-star-half-o"\
                                     aria-hidden="true"></span></a></li>\
               <li><a href="#"><span class="fa fa-star-half-o"\
                                     aria-hidden="true"></span></a></li>\
               <li><a href="#"><span class="fa fa-star-o"\
                                     aria-hidden="true"></span></a>\
               </li>\
           </ul>\
       </div>\
   </div>\
</div>\
{{/movies}}';