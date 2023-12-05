'use client'

export default function CardVideos ({video}){
    return (
        <div className="w3-col l4 m6 s12 w3-container w3-padding-16">
            <div className="w3-card">
                <div className="w3-container w3-center">
                <iframe width="560" height="315" src={video.url.replace("https://www.youtube.com/watch?v=", 'https://www.youtube.com/embed/')} title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    <h5>{video.name}</h5>
                    <h3 className="w3-blue">
                    </h3>
                </div>
            </div>
        </div>
    )
}

