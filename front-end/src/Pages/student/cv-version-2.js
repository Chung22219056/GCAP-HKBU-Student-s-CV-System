
import React from 'react';
import './cv-version-2.css'


export default function Cv2() {
    return (
        <>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"></link>
            <div className="box-outer">
                <div className="resume-box">
                    <div className="box-1">
                        <img src="../pic.jpg" className="profile" />
                        <div className="content">
                            <h1>About me</h1>
                            <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,

                            </p>

                            <br />
                            <h1>Award</h1>
                            <p><span style={{ 'color': 'white' }}>Lorem Ipsum </span>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy
                                <br /><br />
                                <span style={{ 'color': 'white' }}>text ever </span> the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

                            </p>
                            <br />
                            <h1>Contact</h1>

                            <p><i className="fa fa-map"></i> &nbsp;LON,United Kingdom </p>
                            <p><i className="fa fa-phone"></i> &nbsp;phone +(91)1 234 3455</p>
                            <p><i className="fa fa-envelope"></i> &nbsp;email : demo@gmail.com</p>
                            <p><i className="fa fa-globe"></i> &nbsp;www.m-softtech.in</p>

                        </div>

                    </div>

                    <div className="box-2">

                        <div className="intro">

                            <br />
                            <h1 className="ma">Manoj</h1>
                            <h1> <strong>Adhikari</strong></h1>

                            <p className="phead">Graphic Designer</p>
                            <div className="clearfix"></div>
                            <hr className="hr1" />
                        </div>

                        <br /><br /><br />
                        <div className="content-2">
                            <h1 className="head">Experience</h1>
                            <hr className="hr2" />
                            <div className="clearfix"></div>
                            <p className="para-1">UI Designer In Lorem Ipsum <strong>(2018 - Now)</strong></p>
                            <p className="para-21">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been.</p>

                            <p className="para-1">UI Designer <strong>(2013 - 2015)</strong></p>
                            <p className="para-21">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s</p>

                            <p className="para-1">Grapic Designer<strong>(2010)</strong></p>
                            <p className="para-21">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been</p>
                        </div>


                        <div className="content-2">
                            <h1 className="head">Education</h1>
                            <hr className="hr2" />
                            <div className="clearfix"></div>
                            <p className="para-1">High school of cbse <strong>(2009 - 2010)</strong></p>
                            <p className="para-21">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been</p>

                            <p className="para-1">Bachelor of Computer Application <strong>(2013 - 2015)</strong></p>
                            <p className="para-21">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s</p>


                        </div>

                        <h1 className="head">Skills</h1>
                        <hr className="hr2" />

                        <div className="container">
                            <div className="row">
                                <div className="clearfix"></div>
                                <div className="col-div-4">
                                    <p className="p25">HTML</p>
                                </div>

                                <div className="clearfix"></div>
                                <div className="col-div-4">
                                    <p className="p25">CSS</p>
                                </div>

                                <div className="clearfix"></div>
                                <div className="col-div-4">
                                    <p className="p25">JQUERY</p>
                                </div>

                                <div className="clearfix"></div>
                                <div className="col-div-4">
                                    <p className="p25">JAVASCRIPT</p>
                                </div>

                            </div>
                        </div>

                    </div>

                </div>
                <div className="clearfix"></div>
            </div>

        </>
    );
}


