'use client'

export default function CardVideos ({video}){
    return (
        <div className="w3-col l4 m6 s12 w3-container w3-padding-16">
            <div className="w3-card">
            <div className="min-w-0 flex-auto">
            <p className="text-sm font-semibold leading-6 text-gray-900">
            <h5>{video.name}</h5>
            </p>
            </div>
                <div className="w3-container w3-center">
                <div className="video-responsive">
                    <iframe
                    width="480"
                    height="480"
                    src={`${video.url}`}
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowFullScreen
                    title="Embedded youtube"
                    />
                </div>                    <h3 className="w3-blue">
                    </h3>
                </div>
            </div>
        </div>
    )
}


