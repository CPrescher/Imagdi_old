import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { KaraboDataComponent } from './karabo-data.component';

describe('KaraboDataComponent', () => {
  let component: KaraboDataComponent;
  let fixture: ComponentFixture<KaraboDataComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ KaraboDataComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(KaraboDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
