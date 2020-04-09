import { BrowserModule } from '@angular/platform-browser';
import { CommonModule } from '@angular/common';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HeaderComponent } from './header/header.component';
import { FileComponent } from './file/file.component';
import { KaraboDataComponent } from './karabo-data/karabo-data.component';
import { PlotComponent } from './plot/plot.component';
import { MaterialsModule } from './materials.module';
import { KaraboBridgeComponent } from './karabo-bridge/karabo-bridge.component';

import { PlotlyViaWindowModule } from 'angular-plotly.js';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FileComponent,
    KaraboDataComponent,
    PlotComponent,
    KaraboBridgeComponent,
  ],
  imports: [
    CommonModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MaterialsModule,
    PlotlyViaWindowModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
