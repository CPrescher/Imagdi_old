import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KaraboBridgeComponent } from './karabo-bridge.component';

describe('KaraboBridgeComponent', () => {
  let component: KaraboBridgeComponent;
  let fixture: ComponentFixture<KaraboBridgeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KaraboBridgeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KaraboBridgeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
